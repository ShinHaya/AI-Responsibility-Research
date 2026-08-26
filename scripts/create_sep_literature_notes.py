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
            "<!-- concept-provenance-note:start -->",
            "> [!info]- 概念の来歴",
            "> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。",
            "> **分析哲学の標準概念**：該当なし。",
            "> **隣接分野・文献由来**：該当なし。",
            "> **本研究による再構成**：該当なし。",
            "> **本研究で導入した作業概念**：該当なし。",
            "> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。",
            "> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。",
            "> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。",
            "> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。",
            "<!-- concept-provenance-note:end -->",
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
            "<!-- section-provenance:source -->",
            f"**出自**：文献由来（@{citekey}の内容を要約する欄。翻訳・要約の表現はノート作成者による）。",
            "",
            "## Key Claims",
            "",
            "<!-- section-provenance:source -->",
            f"**出自**：文献由来（@{citekey}の内容を要約する欄。翻訳・要約の表現はノート作成者による）。",
            "",
            "## Relevance to My Theory",
            "",
            "<!-- section-provenance:project -->",
            "**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。",
            "",
            "## My Evaluation",
            "",
            "<!-- section-provenance:project -->",
            "**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。",
            "",
            "### Agree",
            "",
            "### Disagree / Problems",
            "",
            "### Extension",
            "",
            "## Related Concepts",
            "",
            "<!-- section-provenance:curation -->",
            "**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。",
            "",
            "## Related Arguments",
            "",
            "<!-- section-provenance:curation -->",
            "**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。",
            "",
            "## Questions Raised",
            "",
            "<!-- section-provenance:project -->",
            "**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。",
            "",
            "## Notes",
            "",
            "<!-- section-provenance:curation -->",
            "**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。",
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
