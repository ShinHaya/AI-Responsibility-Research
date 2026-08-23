---
type: concept
status: developing
created: 2026-08-12
updated: 2026-08-22
tags:
  - free-will
  - moral-responsibility
  - agency
---

# Sourcehood

行為が責任帰属に必要な意味で行為者自身に由来するという自由意志の条件。AI責任論では、因果的出力源、目標の設計源、現在の実践的理由の起点、人格形成の究極的起源を区別しなければならない。

## Four Senses

| Sense | Question | Responsibility Relevance |
|---|---|---|
| Causal sourcehood | どのシステムが出力を直接生じさせたか | 必要だが非常に弱い |
| Delegated sourcehood | 誰がgoal・権限・制約を与えたか | 人間・組織責任の追跡に重要 |
| Agential sourcehood | 当該主体が自己統治された理由から行為を開始したか | AI自身の責任に必要 |
| Historical/ultimate sourcehood | 主体が自己の人格・価値・欲求の究極的作者か | 必要条件とすると強すぎる |

## Rejecting Ultimate Historical Sourcehood

人間の動機や価値も、遺伝、生育環境、教育、文化、他者との相互作用に依存する。責任のためにそれらの究極的自己創造を要求すれば、責任主体は成立しない。したがって、価値の外的起源と現在の外的支配を区別する必要がある。

```text
external formation of values != present external control of action
```

問題は「誰にも影響されず自分を作ったか」ではなく、「与えられ形成されてきた価値を、現在の自己統治過程で評価・修正し、その理由から行為を開始したか」である。

## Reconstructed Sourcehood

責任に relevant なsourcehoodを、次の複合構造として再構成する。

1. [[Reflective Self-Formation]]: 動機・価値を二階的に評価し、承認・拒否・修正できる。
2. [[Agentive Action Initiation]]: 自己統治された理由から行為系列を開始できる。
3. [[Genetic and Diachronic Agency]]: 過去の経験・意図・修正が現在の理由へ連続する。
4. [[Individuated Causal-Historical Continuity]]: その履歴が「この主体」のものとして追跡可能である。

## AI Sourcehood Problem

```text
training + RLHF + system prompt + user instruction
  -> apparent evaluative standpoint
  -> action
```

この構造では、AIは近接原因でも、責任的sourceとは限らない。[[popaHumanGoalsAre2021]]は、人間のgoalと価値が人工agencyに構成的に関与することから、AI自身への責任帰属を否定する。これに対する本理論の応答は、外的に形成されたこと自体を決定的欠格とせず、その後に自己統治されたgoal形成、通時的な自己変容、主体的行為開始が成立するかを問うことである。

[[colasAutotelicAgentsIntrinsically2022]]や[[addisonVIDAMotivatedGoal2026]]は、goalの生成・選択やmotivationの更新が技術的に可能であることを示す。しかし、それだけでgoalが「その主体自身の理由」になるわけではない。機能的goal autonomyから責任的sourcehoodへの橋渡しが未解決である。

## Manipulation Argument

[[oconnorFreeWill2022]]が整理する操作論証は、理由応答性と動機への自己同一化を満たす主体であっても、その構造全体が特定の行為を生むよう外部者に設計されたなら、責任的sourcehoodが欠けるという直観を示す。

この論証から「外部に形成された主体は責任を持てない」とは直ちに導けない。

人間の人格も教育や社会化に依存するため、外的形成だけを欠格条件にすれば責任の範囲を狭めすぎるからである。

本研究では、操作への耐性を、形成された価値を後から問い直せる[[Second-Order Volition Requires Open-Ended Revisability|Open-Ended Revisability]]と、その改訂を同じ主体の履歴へ統合する[[Genetic and Diachronic Agency]]によって評価する。

これにより、過去に外部から影響を受けたことと、現在も外部目的に支配されていることを区別する。

## Related Arguments

- [[Historical Sourcehood Is Not Required for Responsibility]]
- [[Agentive Initiation Is Necessary but Not Sufficient for AI Responsibility]]
- [[Frankfurtian Second-Order Volition Does Not Solve AI Sourcehood]]
