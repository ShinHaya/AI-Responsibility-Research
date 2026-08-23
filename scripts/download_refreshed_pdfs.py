#!/usr/bin/env python3
"""Download and validate the first working public PDF candidate per SEP item."""

from __future__ import annotations

import concurrent.futures
import json
import re
import subprocess
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/sep-freewill/metadata-refresh.json"
OUT = ROOT / "tmp/pdfs/sep-freewill-refresh"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) CodexResearch/1.0"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")[:90]


def attempt(record: dict) -> dict:
    result = {"index": record["index"], "title": record["title"], "status": "no_candidate", "attempts": []}
    target = OUT / f"{record['index']:03d}-{slug(record['title'])}.pdf"
    if target.exists() and target.read_bytes()[:5] == b"%PDF-":
        result.update({"status": "downloaded", "path": str(target), "source_url": "existing"})
        return result
    for url in record.get("pdf_candidates", []):
        entry = {"url": url}
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/pdf,*/*;q=0.8"})
            with urllib.request.urlopen(req, timeout=25) as response:
                body = response.read(25_000_000)
                entry["final_url"] = response.geturl()
                entry["content_type"] = response.headers.get("Content-Type", "")
            if not body.startswith(b"%PDF-"):
                entry["error"] = "not_pdf"
                result["attempts"].append(entry)
                continue
            target.write_bytes(body)
            check = subprocess.run(["pdfinfo", str(target)], capture_output=True, text=True, timeout=20)
            if check.returncode != 0:
                target.unlink(missing_ok=True)
                entry["error"] = "pdfinfo_failed"
                result["attempts"].append(entry)
                continue
            pages = re.search(r"^Pages:\s+(\d+)", check.stdout, re.M)
            entry["pages"] = int(pages.group(1)) if pages else None
            entry["bytes"] = len(body)
            result["attempts"].append(entry)
            result.update({"status": "downloaded", "path": str(target), "source_url": entry["final_url"], "pages": entry["pages"], "bytes": len(body)})
            return result
        except Exception as exc:
            entry["error"] = f"{type(exc).__name__}: {exc}"
            result["attempts"].append(entry)
    if result["attempts"]:
        result["status"] = "failed"
    return result


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    records = json.load(open(SOURCE))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(attempt, records))
    report = ROOT / "data/sep-freewill/pdf-refresh-downloads.json"
    report.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    counts = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
