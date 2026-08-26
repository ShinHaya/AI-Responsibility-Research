---
type: literature
status: unread
citekey: "{{citekey}}"
title: "{{title}}"
authors: "{{authors}}"
year: "{{date | format('YYYY')}}"
doi: "{{DOI}}"
zotero: "{{desktopURI}}"
tags:
  - literature
---

# {{title}}

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：将来のLiterature Note用template。出自表示は新規ノートでも維持する。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：該当なし。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Bibliographic Information

**Citation Key:** @{{citekey}}

**Authors:** {{authors}}

**Year:** {{date | format("YYYY")}}

{% if DOI %}
**DOI:** {{DOI}}
{% endif %}

{% if url %}
**URL:** {{url}}
{% endif %}

{% if pdfZoteroLink %}
**PDF:** {{pdfZoteroLink}}
{% endif %}

{% if bibliography %}
**Citation:** {{bibliography}}
{% endif %}

---

## Abstract

{{abstractNote}}

---

## Core Idea

<!-- section-provenance:source -->
**出自**：文献由来（@{{citekey}}の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

> この文献の中心的主張を、自分の言葉で記述する。

## Key Claims

<!-- section-provenance:source -->
**出自**：文献由来（@{{citekey}}の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

-

## Relevance to My Theory

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

この文献が自分の理論のどのConcept / Argument / Theoryに関係するかを記述する。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

### Agree

-

### Disagree / Problems

-

### Extension

-

## Related Concepts

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

-

## Related Arguments

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

-

## Questions Raised

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

-

## Notes

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

-
