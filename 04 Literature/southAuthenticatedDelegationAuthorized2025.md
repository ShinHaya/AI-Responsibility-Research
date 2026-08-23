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

人間からAIエージェントへの権限委任は、既存のOAuth 2.0とOpenID Connectを拡張し、人間とagentを別々に認証することで監査可能にできる。

## Key Claims

- agent固有のcredentialとmetadataが必要である。
- human principal、agent、委任範囲を分離して記録する必要がある。
- 自然言語による許可は、監査可能なaccess-control configurationへ変換されなければならない。
- 既存のWeb認証基盤との互換性を保った実装が可能である。

## Relevance to My Theory

BYOAIでは同じユーザーが複数agentを利用するため、user IDだけでは行為主体を区別できない。

本稿は[[AI Individuation]]のthin identificationを、認証と委任の技術要件へ接続する。

## My Evaluation

### Agree

- identity、delegation、authorizationを分ける設計に賛成する。
- 役割責任の範囲を機械可読な権限として表現する点は、責任帰属の実装に有効である。

### Disagree / Problems

- 正式に委任された権限が、agentが実際に形成した意図や人間の意味的意図と一致するとは限らない。
- recursive delegationと外部情報による行動変容には、OAuth型記録だけでは対処できない。

### Extension

委任記録を[[Agentic Causal Provenance]]へ組み込み、policy decision、context、tool resultまで因果系列として保存する。

## Related Concepts

- [[AI Individuation]]
- [[Agentic Causal Provenance]]
- [[Responsibility]]

## Related Arguments

- [[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]

## Questions Raised

- 自然言語の委任意図と形式化されたscopeのずれを誰が負担するのか。
- sub-agentへ再委任された場合、principalとの連鎖をどこまで保存すべきか。

## Notes

- Zotero item key: `54MXPQNP`

