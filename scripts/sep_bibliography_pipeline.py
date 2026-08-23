#!/usr/bin/env python3
"""Extract and reconcile the SEP Free Will bibliography.

The extractor preserves the source citation verbatim and derives conservative
metadata for Zotero import.  Ambiguous records remain identifiable through the
source citation instead of receiving invented publication facts.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import difflib
import html
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path


SEP_URL = "https://plato.stanford.edu/entries/freewill/"
ZOTERO_API = "http://127.0.0.1:23119/api/users/0"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


class BibliographyParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_bib = False
        self.in_li = False
        self.depth = 0
        self.parts: list[str] = []
        self.links: list[str] = []
        self.entries: list[tuple[str, list[str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_d = dict(attrs)
        if tag == "div" and attrs_d.get("id") == "bibliography":
            self.in_bib = True
            self.depth = 1
            return
        if not self.in_bib:
            return
        if tag == "div":
            self.depth += 1
        if tag == "li":
            self.in_li = True
            self.parts = []
            self.links = []
        elif self.in_li and tag == "a" and attrs_d.get("href"):
            self.links.append(urllib.parse.urljoin(SEP_URL, attrs_d["href"] or ""))

    def handle_endtag(self, tag: str) -> None:
        if not self.in_bib:
            return
        if tag == "li" and self.in_li:
            text = re.sub(r"\s+", " ", html.unescape("".join(self.parts))).strip()
            self.entries.append((text, self.links.copy()))
            self.in_li = False
        if tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.in_bib = False

    def handle_data(self, data: str) -> None:
        if self.in_li:
            self.parts.append(data)


@dataclass
class Record:
    index: int
    citation: str
    authors_raw: str
    year: str
    title: str
    item_type: str
    urls: list[str]
    normalized_title: str
    matched_zotero_key: str | None = None
    matched_citation_key: str | None = None
    match_method: str | None = None
    status: str = "pending"


def infer_record(index: int, citation: str, urls: list[str], previous_authors: str) -> tuple[Record, str]:
    s = citation.strip()
    repaired = {
        20: re.sub(r",\s+\[1655\]\s+1999\.", ", 1999.", s),
        45: s.replace("2017.\u201c", "2017. \u201c"),
        58: re.sub(r",\s+\[1297–99\]\s+\[1994\]\.", ", 1994.", s),
        204: s.replace(". \u201cIncompatibilism", ", 2009. \u201cIncompatibilism", 1),
        208: s.replace("Pink, Thomas 2017.", "Pink, Thomas, 2017."),
        209: s.replace("Plato (CW/1997).", "Plato, 1997."),
        266: s.replace("van Inwagen, Peter 1975.", "van Inwagen, Peter, 1975."),
        295: s.replace("Wiggins, David 1973.", "Wiggins, David, 1973."),
    }.get(index, s)
    m = re.match(r"(?P<authors>.+?),\s+(?P<year>(?:1[0-9]{3}|20[0-9]{2})(?:[a-z])?(?:\s*\[[^\]]+\])?)\.\s+(?P<body>.+)$", repaired)
    if not m:
        return Record(index, s, "", "", s.rstrip("."), "document", urls, normalize(s)), previous_authors

    authors = m.group("authors").strip()
    if re.fullmatch(r"[-–—]+", authors):
        authors = previous_authors
    else:
        previous_authors = authors
    year = re.match(r"(?:1[0-9]{3}|20[0-9]{2})", m.group("year")).group(0)  # type: ignore[union-attr]
    body = m.group("body").strip()

    quoted = re.match(r"[“\"](?P<title>.+?)[”\"](?P<rest>.*)$", body)
    if quoted:
        title = quoted.group("title").strip().rstrip(".,")
        rest = quoted.group("rest")
        item_type = "bookSection" if re.search(r"\bin\b", rest, re.I) else "journalArticle"
    else:
        title = re.split(r",\s+(?:edited|translated|tr\.|ed\.|[A-Z][^,]+:\s+[A-Z])", body, maxsplit=1)[0]
        title = re.split(r",\s+\d+\s*(?:\(|:)", title, maxsplit=1)[0]
        title = re.sub(r"^\[[A-Z]+\]\s*", "", title).strip().rstrip(".,")
        item_type = "book"

    return Record(index, s, authors, year, title, item_type, urls, normalize(title)), previous_authors


def fetch_json(url: str) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": "Codex SEP bibliography workflow"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def zotero_inventory() -> list[dict]:
    items: list[dict] = []
    start = 0
    while True:
        url = f"{ZOTERO_API}/items/top?format=json&limit=100&start={start}"
        page = fetch_json(url)
        if not isinstance(page, list) or not page:
            break
        items.extend(page)
        if len(page) < 100:
            break
        start += len(page)
    return items


def extract(out: Path) -> None:
    with urllib.request.urlopen(SEP_URL, timeout=30) as response:
        source = response.read().decode("utf-8")
    parser = BibliographyParser()
    parser.feed(source)
    previous = ""
    records: list[Record] = []
    for i, (citation, urls) in enumerate(parser.entries, 1):
        record, previous = infer_record(i, citation, urls, previous)
        records.append(record)

    inventory = zotero_inventory()
    by_title_year: dict[tuple[str, str], list[dict]] = {}
    by_title: dict[str, list[dict]] = {}
    for item in inventory:
        data = item.get("data", item)
        title_n = normalize(str(data.get("title", "")))
        year_m = re.search(r"(?:1[0-9]{3}|20[0-9]{2})", str(data.get("date", "")))
        year = year_m.group(0) if year_m else ""
        if title_n:
            by_title_year.setdefault((title_n, year), []).append(data)
            by_title.setdefault(title_n, []).append(data)

    for record in records:
        candidates = by_title_year.get((record.normalized_title, record.year), [])
        method = "title+year"
        if not candidates:
            candidates = by_title.get(record.normalized_title, [])
            method = "title"
        if len(candidates) == 1:
            item = candidates[0]
            record.matched_zotero_key = item.get("key")
            record.matched_citation_key = item.get("citationKey")
            record.match_method = method
            record.status = "already_in_zotero"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps([asdict(r) for r in records], ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "bibliography_count": len(records),
        "zotero_top_level_count": len(inventory),
        "already_in_zotero": sum(r.status == "already_in_zotero" for r in records),
        "pending": sum(r.status == "pending" for r in records),
        "unparsed": sum(not r.year for r in records),
        "output": str(out),
    }, ensure_ascii=False, indent=2))


def ris_escape(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_authors(raw: str) -> list[str]:
    if not raw:
        return []
    parts = re.split(r"\s+(?:and|&)\s+", raw)
    authors: list[str] = []
    for i, part in enumerate(parts):
        part = part.strip().strip(",")
        if not part:
            continue
        if i == 0 or "," in part:
            authors.append(part)
        else:
            words = part.split()
            authors.append(f"{words[-1]}, {' '.join(words[:-1])}" if len(words) > 1 else part)
    return authors


def make_ris(source: Path, out: Path) -> None:
    records = json.loads(source.read_text())
    blocks: list[str] = []
    type_map = {"journalArticle": "JOUR", "bookSection": "CHAP", "book": "BOOK", "document": "GEN"}
    for r in records:
        if r["status"] != "pending":
            continue
        lines = [f"TY  - {type_map.get(r['item_type'], 'GEN')}", f"TI  - {ris_escape(r['title'])}"]
        for author in parse_authors(r["authors_raw"]):
            lines.append(f"AU  - {ris_escape(author)}")
        if r["year"]:
            lines.append(f"PY  - {r['year']}")
        for url in r["urls"]:
            lines.append(f"UR  - {url}")
        lines.extend([
            f"N1  - SEP Free Will bibliography item {r['index']}: {ris_escape(r['citation'])}",
            "KW  - SEP Free Will Bibliography",
            "ER  -",
        ])
        blocks.append("\n".join(lines))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n\n".join(blocks) + "\n")
    print(json.dumps({"ris_records": len(blocks), "output": str(out)}, ensure_ascii=False, indent=2))


def openalex_candidate(record: dict) -> dict:
    query = urllib.parse.urlencode({
        "search": record["title"],
        "per-page": 5,
        "select": "id,doi,title,publication_year,type,authorships,best_oa_location,open_access",
    })
    url = f"https://api.openalex.org/works?{query}"
    result = {"index": record["index"], "status": "not_found", "query_url": url}
    try:
        data = fetch_json(url)
        candidates = data.get("results", []) if isinstance(data, dict) else []
        best = None
        best_score = 0.0
        for candidate in candidates:
            score = difflib.SequenceMatcher(None, normalize(record["title"]), normalize(candidate.get("title", ""))).ratio()
            candidate_year = candidate.get("publication_year")
            if record.get("year") and candidate_year:
                delta = abs(int(record["year"]) - int(candidate_year))
                if delta > 1:
                    score -= min(0.25, delta * 0.025)
            if score > best_score:
                best, best_score = candidate, score
        if not best or best_score < 0.78:
            result.update({"best_score": round(best_score, 3)})
            return result
        oa = best.get("best_oa_location") or {}
        pdf_url = oa.get("pdf_url")
        result.update({
            "status": "pdf_candidate" if pdf_url else "matched_no_pdf",
            "best_score": round(best_score, 3),
            "openalex_id": best.get("id"),
            "matched_title": best.get("title"),
            "matched_year": best.get("publication_year"),
            "doi": best.get("doi"),
            "pdf_url": pdf_url,
            "landing_page_url": oa.get("landing_page_url"),
            "oa_status": (best.get("open_access") or {}).get("oa_status"),
        })
    except Exception as exc:
        result.update({"status": "error", "error": f"{type(exc).__name__}: {exc}"})
    return result


def find_pdfs(source: Path, out: Path, workers: int) -> None:
    records = json.loads(source.read_text())
    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(openalex_candidate, record) for record in records]
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            results.append(future.result())
            if i % 25 == 0:
                print(f"queried={i}/{len(records)}", flush=True)
    results.sort(key=lambda r: r["index"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    counts: dict[str, int] = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    print(json.dumps({"counts": counts, "output": str(out)}, ensure_ascii=False, indent=2))


def crossref_candidate(record: dict) -> dict:
    query = urllib.parse.urlencode({"query.bibliographic": record["citation"], "rows": 3})
    url = f"https://api.crossref.org/works?{query}"
    result = {"index": record["index"], "status": "not_found", "query_url": url}
    try:
        data = fetch_json(url)
        candidates = data.get("message", {}).get("items", []) if isinstance(data, dict) else []
        best = None
        best_score = 0.0
        for candidate in candidates:
            titles = candidate.get("title") or []
            title = titles[0] if titles else ""
            score = difflib.SequenceMatcher(None, normalize(record["title"]), normalize(title)).ratio()
            years = candidate.get("published-print") or candidate.get("published-online") or candidate.get("issued") or {}
            parts = years.get("date-parts") or []
            candidate_year = parts[0][0] if parts and parts[0] else None
            if record.get("year") and candidate_year:
                delta = abs(int(record["year"]) - int(candidate_year))
                if delta > 1:
                    score -= min(0.25, delta * 0.025)
            if score > best_score:
                best, best_score = candidate, score
        if not best or best_score < 0.78:
            result.update({"best_score": round(best_score, 3)})
            return result
        links = best.get("link") or []
        pdf_links = [link.get("URL") for link in links if "pdf" in str(link.get("content-type", "")).lower() and link.get("URL")]
        titles = best.get("title") or []
        result.update({
            "status": "pdf_candidate" if pdf_links else "matched_no_pdf",
            "best_score": round(best_score, 3),
            "doi": best.get("DOI"),
            "matched_title": titles[0] if titles else None,
            "pdf_url": pdf_links[0] if pdf_links else None,
            "all_pdf_urls": pdf_links,
        })
    except Exception as exc:
        result.update({"status": "error", "error": f"{type(exc).__name__}: {exc}"})
    return result


def find_crossref(source: Path, out: Path, workers: int) -> None:
    records = json.loads(source.read_text())
    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(crossref_candidate, record) for record in records]
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            results.append(future.result())
            if i % 25 == 0:
                print(f"queried={i}/{len(records)}", flush=True)
    results.sort(key=lambda r: r["index"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    counts: dict[str, int] = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    print(json.dumps({"counts": counts, "output": str(out)}, ensure_ascii=False, indent=2))


def safe_slug(value: str, limit: int = 70) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:limit].rstrip("-") or "work"


def download_one(args: tuple[dict, list[str], Path]) -> dict:
    record, urls, out_dir = args
    result = {"index": record["index"], "status": "failed", "attempted_urls": urls}
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (compatible; scholarly personal research)",
                "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.2",
            })
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read(100 * 1024 * 1024 + 1)
                final_url = response.geturl()
                content_type = response.headers.get("Content-Type", "")
            if len(data) > 100 * 1024 * 1024 or not data.startswith(b"%PDF"):
                continue
            path = out_dir / f"{record['index']:03d}-{safe_slug(record['title'])}.pdf"
            path.write_bytes(data)
            result.update({
                "status": "downloaded",
                "pdf_path": str(path),
                "source_url": url,
                "final_url": final_url,
                "content_type": content_type,
                "size_bytes": len(data),
            })
            return result
        except Exception as exc:
            result["last_error"] = f"{type(exc).__name__}: {exc}"
    return result


def download_pdfs(source: Path, openalex: Path, crossref: Path, out_dir: Path, manifest: Path, workers: int) -> None:
    records = {r["index"]: r for r in json.loads(source.read_text())}
    candidates: dict[int, list[str]] = {}
    for path in (openalex, crossref):
        for result in json.loads(path.read_text()):
            if result.get("pdf_url"):
                candidates.setdefault(result["index"], []).append(result["pdf_url"])
            for url in result.get("all_pdf_urls") or []:
                candidates.setdefault(result["index"], []).append(url)
    for index in list(candidates):
        candidates[index] = list(dict.fromkeys(candidates[index]))
    out_dir.mkdir(parents=True, exist_ok=True)
    jobs = [(records[index], urls, out_dir) for index, urls in sorted(candidates.items())]
    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for result in concurrent.futures.as_completed([pool.submit(download_one, job) for job in jobs]):
            results.append(result.result())
    results.sort(key=lambda r: r["index"])
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "candidate_records": len(jobs),
        "downloaded": sum(r["status"] == "downloaded" for r in results),
        "failed": sum(r["status"] != "downloaded" for r in results),
        "manifest": str(manifest),
    }, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)
    ex = sub.add_parser("extract")
    ex.add_argument("--out", type=Path, required=True)
    ris = sub.add_parser("make-ris")
    ris.add_argument("--source", type=Path, required=True)
    ris.add_argument("--out", type=Path, required=True)
    pdfs = sub.add_parser("find-pdfs")
    pdfs.add_argument("--source", type=Path, required=True)
    pdfs.add_argument("--out", type=Path, required=True)
    pdfs.add_argument("--workers", type=int, default=4)
    crossref = sub.add_parser("find-crossref")
    crossref.add_argument("--source", type=Path, required=True)
    crossref.add_argument("--out", type=Path, required=True)
    crossref.add_argument("--workers", type=int, default=3)
    download = sub.add_parser("download-pdfs")
    download.add_argument("--source", type=Path, required=True)
    download.add_argument("--openalex", type=Path, required=True)
    download.add_argument("--crossref", type=Path, required=True)
    download.add_argument("--out-dir", type=Path, required=True)
    download.add_argument("--manifest", type=Path, required=True)
    download.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()
    if args.command == "extract":
        extract(args.out)
    elif args.command == "make-ris":
        make_ris(args.source, args.out)
    elif args.command == "find-pdfs":
        find_pdfs(args.source, args.out, args.workers)
    elif args.command == "find-crossref":
        find_crossref(args.source, args.out, args.workers)
    elif args.command == "download-pdfs":
        download_pdfs(args.source, args.openalex, args.crossref, args.out_dir, args.manifest, args.workers)


if __name__ == "__main__":
    main()
