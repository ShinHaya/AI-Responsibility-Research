---
type: literature
status: read
citekey: addisonVIDAMotivatedGoal2026
title: "La VIDA: Towards a Motivated Goal Reasoning Agent (Abstract Reprint)"
authors: [Ursula Addison]
year: 2026
publication: Proceedings of the AAAI Conference on Artificial Intelligence
doi: 10.1609/aaai.v40i47.41367
zotero: BASAUA9Z
positions: []
concepts: [Agentive Action Initiation, Reflective Self-Formation]
arguments: [Agentive Initiation Is Necessary but Not Sufficient for AI Responsibility]
thinkers: []
tags: [goal-reasoning, motivation, autonomous-agents]
---

# La VIDA: Towards a Motivated Goal Reasoning Agent

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Genetic and Diachronic Agency]]、[[Reflective Self-Formation]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Bibliographic Information

- Author: Ursula Addison
- Year: 2026
- Proceedings: AAAI 40(47), 39852
- DOI: 10.1609/aaai.v40i47.41367
- Zotero item key: `BASAUA9Z`

## Abstract

La VIDA augments a goal-reasoning agent with a motivation system. When existing goals become invalid, the agent can select new goals that combine utility with motivational concordance. Its motivation system changes incrementally over its operational lifespan in response to goal-reasoning and goal-pursuit experience.

## Core Thesis

<!-- section-provenance:source -->
**出自**：文献由来（@addisonVIDAMotivatedGoal2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

長期運用されるagentには、goalの失効時に外部指示を待たず、新しいgoalを選ぶ能力が必要である。その選択はutilityだけでなく、agentのmotivationとの整合性によって制約され、motivation自体も経験に応じて更新される。

## Key Claims

<!-- section-provenance:source -->
**出自**：文献由来（@addisonVIDAMotivatedGoal2026の内容を要約する欄。翻訳・要約の表現はノート作成者による）。

- goal reasoningはgoal追求ではなく、何を追求するかのdeliberationを扱う。
- motivational concordanceはgoal選択の追加基準になる。
- motivation systemは運用履歴を通じて漸進的に変化する。
- motivated variantはbaselineより有用なgoalを選択する傾向を示す。

## Dialectical Position

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

[[maynordDataDrivenGoalGeneration2013]]のgoal generationと[[colasAutotelicAgentsIntrinsically2022]]のintrinsic motivationを接続し、[[Genetic and Diachronic Agency]]に近い経験依存のmotivation updateを部分的に実装する。

## My Evaluation

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

責任主体論にとって特に重要なのは、motivationが固定パラメータではなく履歴により変化する点である。ただし、更新が「自己の動機を問い直す」反省なのか、性能適応なのかは区別されていない。

```text
adaptive motivation update
  != second-order endorsement
  != open-ended self-critique
```

La VIDAは[[Reflective Self-Formation]]と[[Genetic and Diachronic Agency]]の工学的近似候補だが、責任的sourcehoodの実現例ではない。

## Questions Raised

<!-- section-provenance:project -->
**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。

- motivation updateの評価基準を誰が設定するか。
- goal-self concordanceのselfはどの時間幅と履歴によって個体化されるか。
- 社会規範とのalignmentと自律的な規範批判を両立できるか。
