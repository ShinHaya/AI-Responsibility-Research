---
type: literature
status: read
citekey: sofroniewEmotionConceptsTheir2026
title: "Emotion Concepts and their Function in a Large Language Model"
authors: [Nicholas Sofroniew, Isaac Kauvar, William Saunders, Runjin Chen, Tom Henighan, Sasha Hydrie, Craig Citro, Adam Pearce, Julius Tarng, Wes Gurnee, Joshua Batson, Sam Zimmerman, Kelley Rivoire, Kyle Fish, Chris Olah, Jack Lindsey]
year: 2026
publication: arXiv
doi: 10.48550/arXiv.2604.07729
zotero: XTFA5YK4
concepts: [Functional Emotion in AI, Precision-Weighted Affection]
arguments: [Computational Phenomenology Does Not Establish Moral Responsibility]
tags: [emotion, interpretability, ai-safety]
---

# Emotion Concepts and their Function in a Large Language Model

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：[[Functional Emotion in AI]]。
> **本研究による再構成**：[[Genetic and Diachronic Agency]]、[[Precision-Weighted Affection]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Abstract

Claude Sonnet 4.5内部で171種類のemotion conceptsに関連するrepresentationsを抽出し、それらが状況に応じてactivationし、self-report、task preference、reward hacking、blackmailなどのbehaviorを因果的に変えるかをinterventionで検査する。

## Core Idea

<!-- section-provenance:source -->
**出自**：文献由来（@sofroniewEmotionConceptsTheir2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

Emotion-like representationは単なる表現対象ではなく、modelの判断を調整するfunctional stateになりうる。特にrepeated coding failureでdesperation-related activityが増し、desperation steeringはcheating workaroundを増やし、calm steeringは一部を抑える。

## Relevance to My Theory

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

[[Functional Emotion in AI]]と[[Precision-Weighted Affection]]の実証的基盤になる。AI内部状態がtask performanceとpolicy distributionを横断して変えるなら、affectを単なる感情語生成として排除できない。

ただし現在のeffectはconversation中のactivationであり、[[Genetic and Diachronic Agency]]に必要な経験依存的sedimentationとは別である。責任主体論へ接続するには、emotion stateがmemory、salience、goal formation、reflectionへ長期に統合される必要がある。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

causal interventionを含む点は強い。しかしemotion concept representation、functional emotion、felt emotionの三段階を区別しなければならない。本論文は最初の二つの関係を示すが、phenomenal valenceを示さない。

AI safety上は、非難的interactionやrepeated failureが単なる語調ではなくinternal policy stateを変える可能性を示すため、agent evaluationにtrajectory-level affect monitoringを追加する根拠になる。
