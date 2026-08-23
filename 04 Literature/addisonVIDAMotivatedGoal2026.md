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

## Bibliographic Information

- Author: Ursula Addison
- Year: 2026
- Proceedings: AAAI 40(47), 39852
- DOI: 10.1609/aaai.v40i47.41367
- Zotero item key: `BASAUA9Z`

## Abstract

La VIDA augments a goal-reasoning agent with a motivation system. When existing goals become invalid, the agent can select new goals that combine utility with motivational concordance. Its motivation system changes incrementally over its operational lifespan in response to goal-reasoning and goal-pursuit experience.

## Core Thesis

長期運用されるagentには、goalの失効時に外部指示を待たず、新しいgoalを選ぶ能力が必要である。その選択はutilityだけでなく、agentのmotivationとの整合性によって制約され、motivation自体も経験に応じて更新される。

## Key Claims

- goal reasoningはgoal追求ではなく、何を追求するかのdeliberationを扱う。
- motivational concordanceはgoal選択の追加基準になる。
- motivation systemは運用履歴を通じて漸進的に変化する。
- motivated variantはbaselineより有用なgoalを選択する傾向を示す。

## Dialectical Position

[[maynordDataDrivenGoalGeneration2013]]のgoal generationと[[colasAutotelicAgentsIntrinsically2022]]のintrinsic motivationを接続し、[[Genetic and Diachronic Agency]]に近い経験依存のmotivation updateを部分的に実装する。

## My Evaluation

責任主体論にとって特に重要なのは、motivationが固定パラメータではなく履歴により変化する点である。ただし、更新が「自己の動機を問い直す」反省なのか、性能適応なのかは区別されていない。

```text
adaptive motivation update
  != second-order endorsement
  != open-ended self-critique
```

La VIDAは[[Reflective Self-Formation]]と[[Genetic and Diachronic Agency]]の工学的近似候補だが、責任的sourcehoodの実現例ではない。

## Questions Raised

- motivation updateの評価基準を誰が設定するか。
- goal-self concordanceのselfはどの時間幅と履歴によって個体化されるか。
- 社会規範とのalignmentと自律的な規範批判を両立できるか。

