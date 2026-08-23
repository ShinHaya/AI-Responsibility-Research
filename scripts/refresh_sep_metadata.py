#!/usr/bin/env python3
"""Re-search SEP bibliography metadata, abstracts, and openly accessible PDFs."""

from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 CodexResearch/1.0"


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", value).casefold())


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def request(url: str, *, accept: str = "text/html,application/xhtml+xml,application/pdf", timeout: int = 12, retries: int = 1) -> tuple[bytes, str, str]:
    headers = {"Accept": accept}
    if not url.startswith("http://127.0.0.1:23119/"):
        headers["User-Agent"] = UA
    req = urllib.request.Request(url, headers=headers)
    error = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read(8_000_000), response.headers.get("Content-Type", ""), response.geturl()
        except Exception as exc:
            error = exc
            time.sleep(0.3 * (attempt + 1))
    raise error  # type: ignore[misc]


def json_request(url: str) -> dict:
    body, _, _ = request(url, accept="application/json", timeout=20, retries=3)
    return json.loads(body)


def invert_abstract(index: dict | None) -> str:
    if not index:
        return ""
    positions = [(position, word) for word, offsets in index.items() for position in offsets]
    return " ".join(word for _, word in sorted(positions))


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}
        self.links: list[str] = []
        self.jsonld: list[str] = []
        self._jsonld = False
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k.casefold(): v or "" for k, v in attrs}
        if tag == "meta":
            key = (data.get("name") or data.get("property") or "").casefold()
            if key and data.get("content"):
                self.meta[key] = html.unescape(data["content"]).strip()
        elif tag == "a" and data.get("href"):
            self.links.append(data["href"])
        elif tag == "script" and "ld+json" in data.get("type", "").casefold():
            self._jsonld = True
            self._parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._jsonld:
            self.jsonld.append("".join(self._parts))
            self._jsonld = False

    def handle_data(self, data: str) -> None:
        if self._jsonld:
            self._parts.append(data)


def clean_abstract(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", " ", value or ""))
    value = re.sub(r"^\s*(?:abstract|summary)\s*[:.-]?\s*", "", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip()


def valid_abstract(value: str) -> bool:
    low = value.casefold()
    generic = ("cookie", "javascript", "subscribe", "all rights reserved", "homepage")
    return len(value) >= 120 and not any(word in low for word in generic)


def unwrap_ddg(url: str) -> str:
    parsed = urllib.parse.urlparse(html.unescape(url))
    query = urllib.parse.parse_qs(parsed.query)
    return urllib.parse.unquote(query.get("uddg", [url])[0])


def ddg_results(title: str) -> tuple[str, list[str]]:
    query = f'"{title}" (pdf OR abstract)'
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query})
    try:
        body, _, _ = request(url)
    except Exception:
        return url, []
    parser = PageParser()
    parser.feed(body.decode("utf-8", "replace"))
    links = []
    for raw in parser.links:
        candidate = unwrap_ddg(urllib.parse.urljoin(url, raw))
        if candidate.startswith("http") and "duckduckgo.com" not in candidate and candidate not in links:
            links.append(candidate)
    return url, links[:8]


def page_candidates(url: str, expected_title: str) -> dict:
    result = {"url": url, "abstracts": [], "pdf_urls": []}
    try:
        body, content_type, final_url = request(url)
        result["final_url"] = final_url
        if body.startswith(b"%PDF-") or "application/pdf" in content_type.casefold():
            result["pdf_urls"].append(final_url)
            return result
        parser = PageParser()
        parser.feed(body.decode("utf-8", "replace"))
        page_title = parser.meta.get("citation_title") or parser.meta.get("og:title") or parser.meta.get("dc.title") or ""
        title_score = similarity(expected_title, page_title) if page_title else 0.0
        for key in ("citation_abstract", "eprints.abstract", "dc.description", "dcterms.abstract", "prism.teaser"):
            abstract = clean_abstract(parser.meta.get(key, ""))
            if valid_abstract(abstract):
                result["abstracts"].append({"text": abstract, "source": final_url, "field": key, "title_score": round(title_score, 3)})
        description = clean_abstract(parser.meta.get("description") or parser.meta.get("og:description") or "")
        if valid_abstract(description) and (title_score >= 0.8 or b">Abstract<" in body or b">ABSTRACT<" in body):
            result["abstracts"].append({"text": description, "source": final_url, "field": "description", "title_score": round(title_score, 3)})
        for raw in parser.jsonld:
            try:
                data = json.loads(raw)
            except Exception:
                continue
            nodes = data if isinstance(data, list) else ([data] if isinstance(data, dict) else [])
            for node in nodes:
                if not isinstance(node, dict):
                    continue
                abstract = clean_abstract(node.get("abstract") or "")
                if valid_abstract(abstract):
                    result["abstracts"].append({"text": abstract, "source": final_url, "field": "jsonld.abstract", "title_score": round(title_score, 3)})
        for raw in parser.links:
            candidate = urllib.parse.urljoin(final_url, html.unescape(raw))
            if re.search(r"(?:\.pdf(?:$|[?#])|/pdf(?:$|[?#])|download.*pdf)", candidate, re.I):
                if candidate not in result["pdf_urls"]:
                    result["pdf_urls"].append(candidate)
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def crossref_lookup(doi: str) -> dict:
    if not doi:
        return {}
    try:
        message = json_request("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))["message"]
        return {
            "doi": message.get("DOI"),
            "title": (message.get("title") or [""])[0],
            "abstract": clean_abstract(message.get("abstract", "")),
            "url": message.get("URL"),
            "pdf_urls": [x.get("URL") for x in message.get("link", []) if "pdf" in x.get("content-type", "").casefold() and x.get("URL")],
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def crossref_title_lookup(title: str, year: str) -> dict:
    query = urllib.parse.urlencode({"query.title": title, "rows": 5})
    try:
        items = json_request("https://api.crossref.org/works?" + query).get("message", {}).get("items", [])
        best = None
        best_score = 0.0
        for item in items:
            candidate_title = (item.get("title") or [""])[0]
            score = similarity(title, candidate_title)
            issued = (item.get("issued") or {}).get("date-parts") or []
            candidate_year = str(issued[0][0]) if issued and issued[0] else ""
            if year and candidate_year and abs(int(year) - int(candidate_year)) > 1:
                score -= 0.15
            if score > best_score:
                best, best_score = item, score
        if not best or best_score < 0.84:
            return {"best_score": round(best_score, 3)}
        return {
            "doi": best.get("DOI"),
            "title": (best.get("title") or [""])[0],
            "best_score": round(best_score, 3),
            "abstract": clean_abstract(best.get("abstract", "")),
            "url": best.get("URL"),
            "pdf_urls": [x.get("URL") for x in best.get("link", []) if "pdf" in x.get("content-type", "").casefold() and x.get("URL")],
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def openalex_lookup(doi: str) -> dict:
    if not doi:
        return {}
    try:
        data = json_request("https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi, safe=""))
        locations = data.get("locations") or []
        return {
            "title": data.get("title"),
            "abstract": clean_abstract(invert_abstract(data.get("abstract_inverted_index"))),
            "landing_page_url": (data.get("best_oa_location") or {}).get("landing_page_url"),
            "pdf_urls": list(dict.fromkeys(x.get("pdf_url") for x in locations if x.get("pdf_url"))),
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def existing_doi(index: int, zotero_data: dict, crossref_cache: list[dict]) -> str:
    if zotero_data.get("DOI"):
        return zotero_data["DOI"].removeprefix("https://doi.org/")
    cached = crossref_cache[index - 1]
    return (cached.get("doi") or "").removeprefix("https://doi.org/")


def best_abstract(candidates: list[dict], title: str) -> dict | None:
    valid = [x for x in candidates if valid_abstract(x.get("text", ""))]
    if not valid:
        return None
    rank = {"zotero": 5, "publisher.citation_abstract": 4, "crossref": 3, "openalex": 2, "description": 1}
    valid.sort(key=lambda x: (rank.get(x.get("kind", ""), 0), len(x["text"])), reverse=True)
    return valid[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=298)
    ap.add_argument("--delay", type=float, default=0.7)
    ap.add_argument("--out", default="data/sep-freewill/metadata-refresh.json")
    args = ap.parse_args()
    bibliography = json.load(open(ROOT / "data/sep-freewill/bibliography.json"))
    crossref_cache = json.load(open(ROOT / "data/sep-freewill/crossref-sequential.json"))
    out_path = ROOT / args.out
    existing = {x["index"]: x for x in json.load(open(out_path))} if out_path.exists() else {}

    for record in bibliography[args.start - 1:args.end]:
        idx = record["index"]
        zotero = json_request(f"http://127.0.0.1:23119/api/users/0/items/{record['matched_zotero_key']}")["data"]
        doi = existing_doi(idx, zotero, crossref_cache)
        crossref = crossref_lookup(doi) if doi else crossref_title_lookup(record["title"], record["year"])
        if not doi and crossref.get("doi"):
            doi = crossref["doi"]
        time.sleep(0.15)
        openalex = openalex_lookup(doi)
        search_url, search_links = ddg_results(record["title"])
        inspected = []
        targets = []
        for candidate in [crossref.get("url"), openalex.get("landing_page_url"), *record.get("urls", []), *search_links]:
            if candidate and candidate not in targets:
                targets.append(candidate)
        for url in targets[:2]:
            inspected.append(page_candidates(url, record["title"]))

        abstract_candidates = []
        if zotero.get("abstractNote", "").strip():
            abstract_candidates.append({"text": clean_abstract(zotero["abstractNote"]), "source": "zotero", "kind": "zotero"})
        for kind, source in (("crossref", crossref), ("openalex", openalex)):
            if source.get("abstract"):
                abstract_candidates.append({"text": source["abstract"], "source": source.get("url") or source.get("landing_page_url"), "kind": kind})
        pdf_urls = [*crossref.get("pdf_urls", []), *openalex.get("pdf_urls", [])]
        for page in inspected:
            pdf_urls.extend(page.get("pdf_urls", []))
            for abstract in page.get("abstracts", []):
                abstract_candidates.append({"text": abstract["text"], "source": abstract["source"], "kind": "publisher." + abstract["field"]})
        chosen = best_abstract(abstract_candidates, record["title"])
        result = {
            "index": idx,
            "title": record["title"],
            "year": record["year"],
            "zotero_key": record["matched_zotero_key"],
            "citation_key": record["matched_citation_key"],
            "doi": doi,
            "search_query_url": search_url,
            "search_results": search_links,
            "crossref": crossref,
            "openalex": openalex,
            "inspected_pages": inspected,
            "abstract_candidates": abstract_candidates,
            "chosen_abstract": chosen,
            "pdf_candidates": list(dict.fromkeys(x for x in pdf_urls if x)),
        }
        existing[idx] = result
        ordered = [existing[key] for key in sorted(existing)]
        out_path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"index": idx, "abstract": bool(chosen), "pdf_candidates": len(result["pdf_candidates"])}), flush=True)
        time.sleep(args.delay)


if __name__ == "__main__":
    main()
