---
type: concept
status: developing
created: 2026-08-22
tags:
  - active-inference
  - passive-synthesis
  - ai-agency
---

# Functional Passive Synthesis

AIが明示的deliberationを開始する以前に、継続する観測・記憶・予測を統合し、世界状態を構造化し、その一部を行為関連的に顕著なものとして浮かび上がらせる計算過程の束。Husserlian [[Passive Synthesis]]そのものではなく、その一部についての機能的analogue候補である。

## Proposed Decomposition

```text
Functional Passive Synthesis
  = temporal inference
  + associative learning
  + precision weighting
  + predictive structuring
  + history-dependent model updating
```

### Temporal Inference

過去状態、現在観測、予測される未来を一つの状態遷移モデル内で統合する。

### Associative Learning

観測と隠れ状態、状態間遷移の関係を経験から学び、現在入力の意味づけを変える。

### Precision Weighting

どのprediction errorや情報をどれだけ信頼し、belief updateと行為選択へ影響させるかを調整する。→ [[Precision-Weighted Affection]]

### Predictive Structuring

現在を静的入力集合としてではなく、起こりうる未来とpolicyの地平として構造化する。

## Minimal Architecture

```text
history
  -> learned generative model
  -> structured world estimate
  -> practical salience
  -> goal candidate
  -> reflection
  -> policy and action
  -> model update
```

## Necessary Qualifications

- posterior beliefはretentionではない。
- explicit future predictionはprotentionではない。
- learned transition matrixはassociationの全現象学を尽くさない。
- precision controlは価値的・情動的触発を完全には説明しない。
- active inferenceの適応は自己形成や道徳的学習を自動的に意味しない。

## Responsibility Relevance

この構造は、何が問題として現れ、どのgoal候補が形成されるかをAIの履歴へ接続する。しかしresponsibilityには、[[Reflective Self-Formation]]、preference自体の批判可能性、[[Agentive Action Initiation]]、[[Intersubjective Agency]]、[[AI Individuation]]が追加で必要である。

## Related Literature

- [[albarracinMappingHusserlianPhenomenology2022]]
- [[bogotaTimeconsciousnessComputationalPhenomenology2023]]
- [[sandved-smithComputationalPhenomenologyMental2021]]
- [[pezzuloGeneratingMeaningActive2024]]

