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

> この文献の中心的主張を、自分の言葉で記述する。

## Key Claims

-

## Relevance to My Theory

この文献が自分の理論のどのConcept / Argument / Theoryに関係するかを記述する。

## My Evaluation

### Agree

-

### Disagree / Problems

-

### Extension

-

## Related Concepts

-

## Related Arguments

-

## Questions Raised

-

## Notes

-