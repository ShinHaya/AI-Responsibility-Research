---
type: literature
status: read
citekey: maynordDataDrivenGoalGeneration2013
title: Data-Driven Goal Generation for Integrated Cognitive Systems
authors: [Michael Maynord, Michael T. Cox, Matt Paisner, Don Perlis]
year: 2013
publication: AAAI Fall Symposium Series - Integrated Cognition
doi: null
zotero: KB9JQRDS
positions: []
concepts: [Agentive Action Initiation]
arguments: [Agentive Initiation Is Necessary but Not Sufficient for AI Responsibility]
thinkers: []
tags: [goal-driven-autonomy, cognitive-architecture, goal-generation]
---

# Data-Driven Goal Generation for Integrated Cognitive Systems

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Agentive Action Initiation]]、[[Frankfurtian Second-Order Volition in AI]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Bibliographic Information

- Authors: Michael Maynord, Michael T. Cox, Matt Paisner, Don Perlis
- Year: 2013
- Proceedings: AAAI Fall Symposium Series, Integrated Cognition, 47-54
- Zotero item key: `KB9JQRDS`

## Abstract

The paper presents MIDCA, a metacognitive dual-cycle architecture for open-world action and unexpected events. It explores machine-learned goal generation and anomaly-guided goal insertion as steps toward agents that do more than pursue externally supplied goals.

## Core Thesis

<!-- section-provenance:source -->
**出自**：文献由来（@maynordDataDrivenGoalGeneration2013の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

自律的agentは、与えられたgoalの達成方法を探索するだけでなく、環境の予測外変化や異常から新しいproblemを認識し、それに応じたgoalを生成・管理できなければならない。

## Key Claims

<!-- section-provenance:source -->
**出自**：文献由来（@maynordDataDrivenGoalGeneration2013の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

- Goal pursuitとgoal generationは異なる自律性の次元である。
- 予測と現実の不一致がproblem recognitionを駆動する。
- metacognitive cycleは認知cycleを監視し、goal insertionを調整する。
- open worldではgoalは固定的でなく、生成・変形・放棄される。

## Dialectical Position

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

[[Agentive Action Initiation]]のproblem discoveryからgoal formationまでに直接対応する。
[[colasAutotelicAgentsIntrinsically2022]]はgoal空間とintrinsic motivationを拡張し、[[addisonVIDAMotivatedGoal2026]]はgoal選択をmotivation systemへ接続する。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

この文献は「AIの行為は必ず人間promptから始まる」という主張への明確な反例になる。しかしMIDCAのgoal生成はmission、期待モデル、異常検知機構に依存する。したがって、技術的なproblem discoveryを責任的sourcehoodと同一視してはならない。

責任論上重要なのは、生成されたgoalが二階的評価を経て保持され、他のgoalと優先順位づけされ、同じ通時的主体によって行為へ移されるかである。

## Questions Raised

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

- 異常検知から生成されたgoalは「主体自身のgoal」か。
- metacognitive monitoringは[[Frankfurtian Second-Order Volition in AI]]とどこまで対応するか。
- missionとの関係でのみproblemを認識するagentは、外部目的から独立しているか。
