---
type: literature
status: read
citekey: cuadrosGovernedCollaborativeMemory2026
title: "Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems"
authors: [Diego F. Cuadros, Abdoul-Aziz Maiga, Helen Meskhidze, Andre Curtis-Trudel]
year: 2026
publication: arXiv
doi: 10.48550/arXiv.2605.04264
zotero: BB35FAX2
concepts: [AI Individuation, Intersubjective Agency]
arguments: [Memory Possession Is Not Experience Authorship]
tags: [multi-agent, memory-governance, provenance]
---

# Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Distributed Artificial Agent]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Abstract

Persistent memoryがagent、session、versionを越えてbehavior-shapingになると、問題はretrieval accuracyやaccess controlだけではなく、どのmemoryをshared institutional stateとして存続させるかになる。本論文はこれをselection regimeとして捉え、agent-local、shared institutional、archive、project-continuity memoryを分離する。

## Core Idea

<!-- section-provenance:source -->
**出自**：文献由来（@cuadrosGovernedCollaborativeMemory2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

Memory architectureは受動的なstorageではない。何を保持・共有・拒否・訂正・supersedeするかを決めるgovernanceが、multi-agent systemの将来の認識・identity・行為傾向を形成する。

## Key Requirements

<!-- section-provenance:source -->
**出自**：文献由来（@cuadrosGovernedCollaborativeMemory2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

- provenance fidelity
- selection traceability
- version lineage
- epistemic quality
- correction pathways
- role preservation

## Relevance to My Theory

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

[[Memory Possession Is Not Experience Authorship]]をsystem architectureへ接続する。共有memoryに`origin`だけでなく、誰がratify、revise、rejectしたかを残すことで、情報の来歴と各agent固有のreflective appropriationを区別できる。

完全同期したshared memoryが直ちに一つの[[Distributed Artificial Agent]]を作るわけではない。goal formation、reflection、policy controlまで一体化するかを追加で調べる必要がある。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

法的traceabilityには非常に有用だが、provenance metadataだけで一人称的historyやmoral ownershipを作れるわけではない。それでも、AI責任を実装可能な監査対象へ翻訳する不可欠なtechnical prerequisiteである。
