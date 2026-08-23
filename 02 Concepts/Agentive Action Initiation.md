---
type: concept
status: developing
created: 2026-08-12
updated: 2026-08-22
tags:
  - agency
  - ai-responsibility
  - action-theory
---

# Agentive Action Initiation

外部から個別の行為命令を受けることなく、環境・記憶・価値・未完了の意図を統合し、「何を、なぜ、今行うべきか」を主体自身の実践的推論によって決め、行為系列を開始する能力。

## Core Distinctions

### External Trigger vs External Motivation

外部刺激を受けたこと自体は主体性を否定しない。火災を見て救助を始める人間も、センサーが危険を検出して救助を始めるAIも、契機は外部にある。問うべきなのは、刺激から行為へ至る実践的理由が主体内部で形成・評価されたか、それとも外部命令がそのまま実行されたかである。

```text
external trigger -> self-governed reason formation -> action
external command -> delegated task execution
```

### Automatic Activation vs Agential Initiation

cron、イベントリスナー、センサー閾値による起動は、自発的に見えても設計済み条件の機械的充足にすぎない。主体的行為開始には、少なくとも以下が必要となる。

1. 継続的環境認識
2. 顕著性・価値評価
3. 問題発見と目標形成
4. 未完了意図の保持（展望記憶）
5. 複数目標の優先順位管理
6. 「今が実行時点である」という実践的判断
7. 行為系列の開始と結果に応じた修正

## Relation to Sourcehood

[[Sourcehood]]を「人格形成の究極的作者であること」と理解すると、人間も条件を満たせない。ここではsourcehoodを、現在の行為についての局所的かつ実践的な起点性として再構成する。

ただし、近接原因であることだけでも足りない。AIがユーザー命令を内部で複雑に分解して実行しても、目的と理由が全面的に委任されたままなら、AIは因果的起点ではあっても責任的起点ではない。

## Human Example

朝に牛乳がないと気づき、帰宅時に買うという意図を形成し、数時間後に未完了意図を想起し、他の予定と比較して買い物を開始する。このとき、行為開始時点の直接刺激だけでは説明できない。朝の知覚、持続した意図、現在の機会判断が同じ主体の実践的履歴として統合されている。

## AI Architecture

```text
environmental stream
  -> salience evaluation
  -> problem discovery
  -> goal generation
  -> second-order evaluation
  -> intention persistence
  -> goal prioritization
  -> action initiation
  -> outcome monitoring
  -> self-modification
```

[[maynordDataDrivenGoalGeneration2013]]、[[colasAutotelicAgentsIntrinsically2022]]、[[addisonVIDAMotivatedGoal2026]]は、この連鎖の技術的部分が既に部分実装されていることを示す。したがって「現在のAIはpromptがなければ何も始められない」という経験的主張に理論を依存させるべきではない。

## Limits

- 自己生成goalも、設計されたmissionやintrinsic rewardに拘束されうる。
- 行為開始能力は危険なgoalの自律生成も可能にするため、[[Reflective Self-Formation]]を代替しない。
- 一度の自律起動は、時間を越えた同一主体による理由の引受けを保証しない。[[Genetic and Diachronic Agency]]と[[AI Individuation]]が別途必要である。

## Related

- [[Sourcehood]]
- [[Genetic and Diachronic Agency]]
- [[Frankfurtian Second-Order Volition in AI]]
- [[Historical Sourcehood Is Not Required for Responsibility]]
- [[Agentive Initiation Is Necessary but Not Sufficient for AI Responsibility]]

## Active Inference and Embodied Intervention

[[pezzuloGeneratingMeaningActive2024]]のactive inferenceでは、意味は受動的表象ではなく、身体を通じたprediction、探索、介入の循環で生成される。policy selectionは、予測誤差の低減だけでなく、期待される状態へ世界と身体を能動的に合わせるため、[[Agentive Action Initiation]]の実装基盤になりうる。

しかし、policyが選択されたことは、そのgoalの起源をagent自身に帰属できることを意味しない。責任的な行為開始には、外部promptへの応答を越え、履歴から形成された実践的顕著性、競合goalの評価、実行の抑制可能性、行為後のmodel更新が一つの継続的主体に統合される必要がある。active inferenceはaction-selection機構を与えるが、sourcehoodとnormative ownershipは別途示されなければならない。

## Will as Selective Responsiveness

「外部入力へ反応するシステムには意志がない」という基準は、人間にも適用できない。

人間も知覚、身体状態、他者の要求、環境のaffordanceを継続的に受け取るが、そのすべてへ同じように反応しない。

過去の経験から形成された関心と[[Precision-Weighted Affection]]が一部を顕在化させ、未完了意図と価値評価が応答を選別する。

したがって人工意志の候補を評価するときは、promptの有無ではなく次を問う必要がある。

- 入力のどれを行為理由として採用するかを選別できるか。
- 選別基準が一回のcontextではなく通時的履歴から形成されているか。
- 形成されたgoalを保持し、競合goalと比較し、実行を開始または抑制できるか。
- 選別基準そのものを経験と批判によって改訂できるか。

subgoal decompositionは局所的なgoal-directednessを示すが、この通時的な選別構造を単独では示さない。

一方、最初のgoalが外部契機を持つことだけでも人工意志を否定できない。

人間とAIの差は刺激への反応性ではなく、刺激が自己形成された実践的履歴を通じて理由へ変換される仕方にある。
