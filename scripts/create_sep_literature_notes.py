#!/usr/bin/env python3
"""Create blank-analysis Obsidian literature notes from SEP-matched Zotero items."""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIBLIOGRAPHY = ROOT / "data/sep-freewill/bibliography.json"
LITERATURE = ROOT / "04 Literature"


def zotero_item(key: str) -> dict:
    with urllib.request.urlopen(
        f"http://127.0.0.1:23119/api/users/0/items/{key}", timeout=10
    ) as response:
        return json.load(response)


def yaml_string(value: object) -> str:
    return json.dumps(str(value or ""), ensure_ascii=False)


def creators_text(creators: list[dict]) -> str:
    names = []
    for creator in creators:
        if creator.get("name"):
            names.append(creator["name"])
        else:
            name = " ".join(
                part for part in (creator.get("firstName", ""), creator.get("lastName", "")) if part
            )
            if name:
                names.append(name)
    return "; ".join(names)


def first_year(value: str, fallback: str) -> str:
    match = re.search(r"(?:1[5-9]|20)\d{2}", value or "")
    return match.group(0) if match else fallback


def render(entry: dict, item: dict) -> tuple[str, str]:
    data = item["data"]
    citekey = data.get("citationKey") or entry["matched_citation_key"]
    title = data.get("title") or entry["title"]
    authors = creators_text(data.get("creators", [])) or entry.get("authors_raw", "")
    year = first_year(data.get("date", ""), entry.get("year", ""))
    doi = data.get("DOI", "")
    url = data.get("url", "")
    abstract = data.get("abstractNote", "").strip()
    zotero_key = data.get("key") or entry["matched_zotero_key"]

    optional = []
    if doi:
        optional.extend([f"**DOI:** https://doi.org/{doi}", ""])
    if url:
        optional.extend([f"**URL:** {url}", ""])
    optional.extend([f"**Citation:** {entry['citation']}", ""])

    text = "\n".join(
        [
            "---",
            "type: literature",
            "status: unread",
            f"citekey: {yaml_string(citekey)}",
            f"title: {yaml_string(title)}",
            f"authors: {yaml_string(authors)}",
            f"year: {yaml_string(year)}",
            f"doi: {yaml_string(doi)}",
            f"zotero: {yaml_string(f'zotero://select/library/items/{zotero_key}')} ",
            "tags:",
            "  - literature",
            "  - sep-free-will-bibliography",
            "---",
            "",
            f"# {title}",
            "",
            "## Bibliographic Information",
            "",
            f"**Citation Key:** @{citekey}",
            "",
            f"**Authors:** {authors}",
            "",
            f"**Year:** {year}",
            "",
            *optional,
            "---",
            "",
            "## Abstract",
            "",
            abstract,
            "",
            "---",
            "",
            "## Core Idea",
            "",
            "## Key Claims",
            "",
            "## Relevance to My Theory",
            "",
            "## My Evaluation",
            "",
            "### Agree",
            "",
            "### Disagree / Problems",
            "",
            "### Extension",
            "",
            "## Related Concepts",
            "",
            "## Related Arguments",
            "",
            "## Questions Raised",
            "",
            "## Notes",
            "",
        ]
    )
    return citekey, text


def main() -> None:
    bibliography = json.loads(BIBLIOGRAPHY.read_text())
    created = []
    skipped = []
    abstract_count = 0

    for entry in bibliography:
        item = zotero_item(entry["matched_zotero_key"])
        citekey, text = render(entry, item)
        target = LITERATURE / f"{citekey}.md"
        if target.exists():
            skipped.append(citekey)
            continue
        target.write_text(text, encoding="utf-8")
        created.append(citekey)
        if item["data"].get("abstractNote", "").strip():
            abstract_count += 1

    report = {
        "bibliography": len(bibliography),
        "created": len(created),
        "skipped_existing": len(skipped),
        "created_with_abstract": abstract_count,
        "created_citekeys": created,
        "skipped_citekeys": skipped,
    }
    report_path = ROOT / "data/sep-freewill/literature-import-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if not isinstance(value, list)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
