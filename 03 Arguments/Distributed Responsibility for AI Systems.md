---
type: argument
status: seed
created: 2026-08-22
source: conversation
sourceConversation: "[[2026-08-12-AIへの自由意志と責任の帰属可能性]]"
sourceRange: "chars 0-9936"
tags:
  - ai-responsibility
  - distributed-responsibility
---

# Distributed Responsibility for AI Systems

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：[[Moral Crumple Zone]]、[[Responsibility Gap]]。
> **本研究による再構成**：該当なし。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Thesis

Responsibility for harmful AI action should often be distributed across multiple agents and institutions rather than assigned to a single human, organization, or artificial agent.

Human-machine interactionにおけるdistributed responsibilityには、[[strasserDistributedResponsibility2022]]という直接の先行研究がある。

[[dempseyMoralResponsibilityShared2015]]は、shared valuesとcorporate cultureへの参加に応じた責任分配を論じる。

本Argumentの追加点は、これらの議論をLLM、tool、deployment organizationからなる現代のAI systemへ整理して適用する点にある。

## Argument

Modern AI systems involve many contributors:

- foundation model developers
- model providers
- agent framework developers
- deployment organizations
- tool permission designers
- operators
- users
- the AI system itself as causal intermediary

When harm results from the interaction of these layers, assigning all responsibility to the final user or operator is usually misleading.

## Relevance

This argument supports a multi-level analysis of AI responsibility and helps avoid both extremes:

- no one is responsible because the AI acted autonomously
- only the nearest human is responsible because a human must be blamed

## Related

- [[strasserDistributedResponsibility2022]]
- [[dempseyMoralResponsibilityShared2015]]
- [[Moral Crumple Zone]]
- [[Responsibility Gap]]
- [[Organizational Responsibility for AI Deployment]]
- [[Hybrid Human-AI Agency as Responsibility Subject]]
