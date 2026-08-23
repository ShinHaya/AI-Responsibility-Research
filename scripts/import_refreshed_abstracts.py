#!/usr/bin/env python3
"""Build enrichment RIS and copy verified Zotero-bound abstracts into blank Obsidian notes."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
records = json.load(open(ROOT / "data/sep-freewill/metadata-refresh.json"))
bibliography = {x["index"]: x for x in json.load(open(ROOT / "data/sep-freewill/bibliography.json"))}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def authors(raw: str) -> list[str]:
    parts = re.split(r"\s+(?:and|&)\s+", raw or "")
    return [clean(part.strip(",")) for part in parts if clean(part.strip(","))]


blocks = []
doi_only_blocks = []
obsidian_updated = []
for record in records:
    chosen = record.get("chosen_abstract") or {}
    abstract = clean(chosen.get("text", ""))
    source = bibliography[record["index"]]
    type_code = {"journalArticle": "JOUR", "bookSection": "CHAP", "book": "BOOK"}.get(source["item_type"], "GEN")
    lines = [f"TY  - {type_code}", f"TI  - {clean(source['title'])}"]
    for author in authors(source.get("authors_raw", "")):
        lines.append(f"AU  - {author}")
    if source.get("year"):
        lines.append(f"PY  - {source['year']}")
    if record.get("doi"):
        lines.append(f"DO  - {record['doi']}")
    if chosen.get("source"):
        lines.append(f"UR  - {chosen['source']}")
    if not abstract:
        if record.get("doi"):
            lines.extend(
                [
                    f"N1  - Metadata enrichment for existing Zotero item {record['zotero_key']}.",
                    "KW  - SEP Free Will Bibliography",
                    "KW  - SEP Metadata Refresh",
                    "ER  -",
                ]
            )
            doi_only_blocks.append("\n".join(lines))
        continue
    lines.extend(
        [
            f"AB  - {abstract}",
            f"N1  - Metadata enrichment for existing Zotero item {record['zotero_key']}. Abstract source: {chosen.get('source', '')}",
            "KW  - SEP Free Will Bibliography",
            "KW  - SEP Metadata Refresh",
            "ER  -",
        ]
    )
    blocks.append("\n".join(lines))

    note = ROOT / "04 Literature" / f"{record['citation_key']}.md"
    if note.exists():
        text = note.read_text()
        match = re.search(r"(?ms)(^## Abstract\n\n)(.*?)(\n\n---\n)", text)
        if match and not match.group(2).strip():
            note.write_text(text[:match.start(2)] + abstract + text[match.end(2):])
            obsidian_updated.append(record["citation_key"])

ris = ROOT / "data/sep-freewill/abstract-enrichment.ris"
ris.write_text("\n\n".join(blocks) + "\n")
doi_ris = ROOT / "data/sep-freewill/doi-enrichment.ris"
doi_ris.write_text("\n\n".join(doi_only_blocks) + "\n")
old_report_path = ROOT / "data/sep-freewill/abstract-enrichment-report.json"
old_report = json.load(open(old_report_path)) if old_report_path.exists() else {}
all_obsidian_citekeys = sorted(set(old_report.get("obsidian_citekeys", [])) | set(obsidian_updated))
report = {
    "ris_records": len(blocks),
    "doi_only_ris_records": len(doi_only_blocks),
    "obsidian_abstracts_updated": len(all_obsidian_citekeys),
    "obsidian_citekeys": all_obsidian_citekeys,
}
(ROOT / "data/sep-freewill/abstract-enrichment-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({key: value for key, value in report.items() if key != "obsidian_citekeys"}, ensure_ascii=False))
