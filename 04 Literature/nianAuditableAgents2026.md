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

accountabilityは規範的な評価と責任配分、auditabilityはそれを可能にするsystem property、auditingは証拠から行動を再構成するprocessである。

したがって、監査可能性を欠くagent systemにaccountabilityを要求しても運用できない。

## Key Claims

- auditabilityにはaction recoverability、lifecycle coverage、policy checkability、responsibility attribution、evidence integrityが必要である。
- detect、enforce、recoverの単一機構だけでは十分でない。
- 改ざん耐性のある事前実行記録は、実用可能な遅延で導入できる。
- 通常ログが失われても責任関連情報を部分的に復元できる場合がある。

## Relevance to My Theory

本稿は、[[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]のうち、監査可能性がaccountabilityの認識的前提になる点を直接支持する。

## My Evaluation

### Agree

- accountability、auditability、auditingの区別は責任概念の混同を防ぐ。
- 記録だけでなくpolicy照合とevidence integrityを含める点を支持する。

### Disagree / Problems

- auditabilityは責任判断を可能にするが、正しい責任配分を保証しない。
- 記録範囲を広げるほどプライバシーと営業秘密への負担が増える。

### Extension

監査記録を企業がAIへ責任転嫁するためではなく、救済、原因分析、再発防止という企業自身の責任を果たすための基盤として位置づける。

## Related Concepts

- [[Agentic Causal Provenance]]
- [[Responsibility]]

## Related Arguments

- [[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]

## Questions Raised

- auditabilityとdata minimizationをリスク別にどう調整するか。
- 証拠の完全性を誰が監査するのか。

## Notes

- Zotero item key: `NK4FMHUN`

