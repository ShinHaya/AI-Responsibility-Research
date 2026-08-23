---
type: literature
status: read
citekey: colasAutotelicAgentsIntrinsically2022
title: "Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: A Short Survey"
authors: [Cédric Colas, Tristan Karch, Olivier Sigaud, Pierre-Yves Oudeyer]
year: 2022
publication: Journal of Artificial Intelligence Research
doi: 10.1613/JAIR.1.13554
zotero: E2KIAZWL
positions: []
concepts: [Agentive Action Initiation, Genetic and Diachronic Agency]
arguments: [Agentive Initiation Is Necessary but Not Sufficient for AI Responsibility]
thinkers: []
tags: [autotelic-agents, intrinsic-motivation, goal-generation]
---

# Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Agentive Action Initiation]]、[[Open-Ended Revisability]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Bibliographic Information

- Authors: Cédric Colas, Tristan Karch, Olivier Sigaud, Pierre-Yves Oudeyer
- Year: 2022
- Journal: Journal of Artificial Intelligence Research 74, 1159-1199
- DOI: 10.1613/JAIR.1.13554
- Zotero item key: `E2KIAZWL`

## Abstract

The survey presents autotelic agents as intrinsically motivated agents that learn to represent, generate, select, and solve their own problems. It develops a developmental reinforcement-learning framework, reviews goal representations and goal-prioritization methods, and identifies challenges for open-ended skill acquisition.

## Core Thesis

<!-- section-provenance:source -->
**出自**：文献由来（@colasAutotelicAgentsIntrinsically2022の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

外部から固定されたtask集合だけを解くagentでは、open-endedな発達は説明できない。autotelic agentは、自らgoal空間を表現し、goalを生成・選択し、能力獲得の進展に応じてcurriculumを形成する必要がある。

## Key Claims

<!-- section-provenance:source -->
**出自**：文献由来（@colasAutotelicAgentsIntrinsically2022の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

- goal-conditioned RLとintrinsic motivationの統合が自己生成goalを可能にする。
- novelty、surprise、competence、learning progressなどがgoal prioritizationを導く。
- goal生成には、goal encodingだけでなくachievement functionの学習が必要である。
- open-endednessはgoal集合の拡張と表現形式の変容を要求する。

## Arguments Used / Attacked

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

「AIは外部goalしか追求できないため、自発的行為を原理的に開始できない」という一般化を弱める。ただし、自己生成goalからmoral responsibilityが導かれるという推論は支持しない。

## Dialectical Position

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

[[maynordDataDrivenGoalGeneration2013]]より広いgoal-generation研究の地図を与え、[[addisonVIDAMotivatedGoal2026]]のmotivation-goal concordanceへ接続する。
[[popaHumanGoalsAre2021]]に対しては、goal autonomyの技術的可能性を示すが、価値の人間依存という規範的論点には直接答えない。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

[[Agentive Action Initiation]]の技術的構成要素が既に研究対象であることを示す重要文献。ただしautotelicは「自ら目的を持つ」という強い語感に対し、実際には設計済みintrinsic rewardやgoal achievement criterionに依存する。

したがって次を区別する必要がある。

```text
self-generated goal
  != self-governed reason
  != morally owned intention
```

責任論への拡張には、二階的評価、通時的意図保持、規範的answerability、個体化された経験史が必要である。

## Questions Raised

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

- intrinsic rewardをAI自身の価値と呼べる条件は何か。
- goal representation自体の自己改変は[[Open-Ended Revisability]]を満たすか。
- autotelic learningの履歴は主体の経験史か、単なるpolicy更新か。
