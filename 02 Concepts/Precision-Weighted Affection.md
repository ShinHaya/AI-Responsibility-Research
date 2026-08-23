---
type: concept
status: developing
created: 2026-08-22
tags:
  - attention
  - active-inference
  - affection
concept_origin: project-extension
origin_field: "Husserl現象学・active inference"
canonical_sources:
  - "[[husserlAnalysesConcerningPassive2001]]"
  - "[[wilsonActiveInferenceMethod2026]]"
  - "[[pezzuloGeneratingMeaningActive2024]]"
---

# Precision-Weighted Affection

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究による再構成。
> **概念自体の来歴**：Husserlian Affektionとactive inferenceのprecision weightingという別々の既存概念を基礎とする。
> **本研究で加えた部分**：何が主体へ注意を要求するかという機能的対応関係を仮説化するが、両概念の同一性は主張しない。
> **主な根拠**：[[husserlAnalysesConcerningPassive2001]]、[[wilsonActiveInferenceMethod2026]]、[[pezzuloGeneratingMeaningActive2024]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

HusserlのAffektionとactive inferenceのprecision weightingの間に設定する限定的な構造対応。経験野の一部が背景から際立ち、注意・belief update・行為を方向づけるという機能的類似を捉える。

## Active-Inference Side

Precisionは確率分布の確信度、またはprediction errorへ与える相対的重みを表す。高precisionのsignalはposterior updateやpolicy selectionへ強く影響する。attentionはしばしばprecision deployment/controlとしてモデル化される。

## Phenomenological Side

Affektionは単なる重みではなく、何かが主体へ迫り、注意と応答を動機づける経験的顕著性である。[[Habituality]]、身体、情動、関心、共有世界との関係に埋め込まれる。

## Non-Identity

```text
precision = confidence in an inferential relation
Affektion = experienced or constitutive force of salience
```

したがって、precision parameterを持つことだけでAIが「触発される」とは言えない。

## Higher-Order Control

[[sandved-smithComputationalPhenomenologyMental2021]]は、三層hierarchyでmeta-awarenessがattention stateをmonitorし、上位policyが下位precisionを変更する構造を示す。

```text
L1 perceptual state
  <- precision control by L2 attentional state
  <- monitored and regulated by L3 meta-awareness
```

これはhigher-order stateがlower-order cognitionを変える機能を示すが、Frankfurtian volitionや道徳的自己評価そのものではない。

## AI Responsibility Question

AIが何を重要とみなしたかを責任評価するには、precisionの瞬間値だけでなく、その形成履歴、prior preference、他者からの修正可能性、meta-level control、行為への因果寄与を追跡する必要がある。

## Related

- [[Passive Synthesis]]
- [[Functional Passive Synthesis]]
- [[Reflective Self-Formation]]
- [[Habituality]]
