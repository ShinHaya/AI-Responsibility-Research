---
type: literature
status: read
citekey: nianAuditableAgents2026
title: "Auditable Agents"
authors: "Yi Nian et al."
year: "2026"
doi: 10.48550/arXiv.2604.05485
zotero: zotero://select/library/items/NK4FMHUN
tags:
  - literature
  - ai-agents
  - auditability
---

# Auditable Agents

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：[[Responsibility]]。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Agentic Causal Provenance]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Bibliographic Information

**Citation Key:** @nianAuditableAgents2026

**Authors:** Yi Nian, Aojie Yuan, Haiyue Zhang, Jiate Li, Li Li, Xiyang Hu, Hua Wei, Xiongye Xiao, Chaowei Xiao, Yue Zhao

**Year:** 2026

**DOI:** 10.48550/arXiv.2604.05485

**URL:** https://arxiv.org/abs/2604.05485

---

## Abstract

LLM agents call tools, query databases, delegate tasks, and trigger external side effects. The paper distinguishes accountability, auditability, and auditing, and argues that no agent system can be accountable without auditability. It defines five dimensions of agent auditability and three mechanism classes.

---

## Core Thesis

<!-- section-provenance:source -->
**出自**：文献由来（@nianAuditableAgents2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

accountabilityは規範的な評価と責任配分、auditabilityはそれを可能にするsystem property、auditingは証拠から行動を再構成するprocessである。

したがって、監査可能性を欠くagent systemにaccountabilityを要求しても運用できない。

## Key Claims

<!-- section-provenance:source -->
**出自**：文献由来（@nianAuditableAgents2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

- auditabilityにはaction recoverability、lifecycle coverage、policy checkability、responsibility attribution、evidence integrityが必要である。
- detect、enforce、recoverの単一機構だけでは十分でない。
- 改ざん耐性のある事前実行記録は、実用可能な遅延で導入できる。
- 通常ログが失われても責任関連情報を部分的に復元できる場合がある。

## Relevance to My Theory

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

本稿は、[[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]のうち、監査可能性がaccountabilityの認識的前提になる点を直接支持する。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

### Agree

- accountability、auditability、auditingの区別は責任概念の混同を防ぐ。
- 記録だけでなくpolicy照合とevidence integrityを含める点を支持する。

### Disagree / Problems

- auditabilityは責任判断を可能にするが、正しい責任配分を保証しない。
- 記録範囲を広げるほどプライバシーと営業秘密への負担が増える。

### Extension

監査記録を企業がAIへ責任転嫁するためではなく、救済、原因分析、再発防止という企業自身の責任を果たすための基盤として位置づける。

## Related Concepts

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

- [[Agentic Causal Provenance]]
- [[Responsibility]]

## Related Arguments

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

- [[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]

## Questions Raised

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

- auditabilityとdata minimizationをリスク別にどう調整するか。
- 証拠の完全性を誰が監査するのか。

## Notes

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

- Zotero item key: `NK4FMHUN`
