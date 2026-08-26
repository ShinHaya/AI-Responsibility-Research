---
type: literature
status: read
citekey: southAuthenticatedDelegationAuthorized2025
title: "Authenticated Delegation and Authorized AI Agents"
authors: "Tobin South, Samuele Marro, Thomas Hardjono, Robert Mahari, Cedric Deslandes Whitney, Dazza Greenwood, Alan Chan, Alex Pentland"
year: "2025"
doi: 10.48550/arXiv.2501.09674
zotero: zotero://select/library/items/54MXPQNP
tags:
  - literature
  - ai-agents
  - delegation
---

# Authenticated Delegation and Authorized AI Agents

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：[[Responsibility]]。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Agentic Causal Provenance]]、[[AI Individuation]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Bibliographic Information

**Citation Key:** @southAuthenticatedDelegationAuthorized2025

**Authors:** Tobin South, Samuele Marro, Thomas Hardjono, Robert Mahari, Cedric Deslandes Whitney, Dazza Greenwood, Alan Chan, Alex Pentland

**Year:** 2025

**DOI:** 10.48550/arXiv.2501.09674

**URL:** https://arxiv.org/abs/2501.09674

---

## Abstract

The rapid deployment of autonomous AI agents creates urgent challenges around authorization, accountability, and access control in digital spaces. The authors introduce a framework for authenticated, authorized, and auditable delegation of authority to AI agents, extending OAuth 2.0 and OpenID Connect with agent-specific credentials and metadata.

---

## Core Thesis

<!-- section-provenance:source -->
**出自**：文献由来（@southAuthenticatedDelegationAuthorized2025の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

人間からAIエージェントへの権限委任は、既存のOAuth 2.0とOpenID Connectを拡張し、人間とagentを別々に認証することで監査可能にできる。

## Key Claims

<!-- section-provenance:source -->
**出自**：文献由来（@southAuthenticatedDelegationAuthorized2025の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

- agent固有のcredentialとmetadataが必要である。
- human principal、agent、委任範囲を分離して記録する必要がある。
- 自然言語による許可は、監査可能なaccess-control configurationへ変換されなければならない。
- 既存のWeb認証基盤との互換性を保った実装が可能である。

## Relevance to My Theory

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

BYOAIでは同じユーザーが複数agentを利用するため、user IDだけでは行為主体を区別できない。

本稿は[[AI Individuation]]のthin identificationを、認証と委任の技術要件へ接続する。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

### Agree

- identity、delegation、authorizationを分ける設計に賛成する。
- 役割責任の範囲を機械可読な権限として表現する点は、責任帰属の実装に有効である。

### Disagree / Problems

- 正式に委任された権限が、agentが実際に形成した意図や人間の意味的意図と一致するとは限らない。
- recursive delegationと外部情報による行動変容には、OAuth型記録だけでは対処できない。

### Extension

委任記録を[[Agentic Causal Provenance]]へ組み込み、policy decision、context、tool resultまで因果系列として保存する。

## Related Concepts

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

- [[AI Individuation]]
- [[Agentic Causal Provenance]]
- [[Responsibility]]

## Related Arguments

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

- [[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]

## Questions Raised

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

- 自然言語の委任意図と形式化されたscopeのずれを誰が負担するのか。
- sub-agentへ再委任された場合、principalとの連鎖をどこまで保存すべきか。

## Notes

<!-- section-provenance:curation -->
**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。

- Zotero item key: `54MXPQNP`
