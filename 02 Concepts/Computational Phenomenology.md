---
type: concept
status: developing
created: 2026-08-22
tags:
  - computational-phenomenology
  - active-inference
  - methodology
concept_origin: borrowed-adjacent-field
origin_field: "計算論的神経科学・現象学"
canonical_sources:
  - "[[sandved-smithComputationalPhenomenologyMental2021]]"
  - "[[albarracinMappingHusserlianPhenomenology2022]]"
  - "[[bogotaTimeconsciousnessComputationalPhenomenology2023]]"
---

# Computational Phenomenology

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：隣接分野・文献由来。
> **概念自体の来歴**：現象学的構造と計算モデルの対応を探る既存の研究計画である。
> **本研究で加えた部分**：responsible agencyを哲学、機能・計算、規範の三水準で接続する方法へ拡張する。
> **主な根拠**：[[sandved-smithComputationalPhenomenologyMental2021]]、[[albarracinMappingHusserlianPhenomenology2022]]、[[bogotaTimeconsciousnessComputationalPhenomenology2023]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

現象学が記述する経験構造を、計算モデルが満たすべき構造的制約へ翻訳し、形式化・simulation・mechanistic evaluationへ接続する研究方法。目的は現象学用語を計算用語へ置換することではなく、経験記述と計算機構の間に検証可能なmappingを構築することである。

## Methodological Pipeline

```text
phenomenological description
  -> structural constraint
  -> functional decomposition
  -> formal model
  -> computational implementation
  -> behavioral and mechanistic evaluation
  -> limited normative inference
```

[[albarracinMappingHusserlianPhenomenology2022]]と[[bogotaTimeconsciousnessComputationalPhenomenology2023]]は、Husserlの時間意識とactive inferenceの生成モデルを対応づけるmethodological precedentを与える。

## Mapping Is Not Identity

```text
retention-like dependence != experienced retention
protention-like prediction != experienced protention
precision weighting != Affektion
Bayesian state integration != passive synthesis as a whole
```

構造的類似は、現象的意識、personhood、moral normativity、responsibilityを自動的に与えない。計算モデルが現象学的構造の一部を実装しても、それが「現れる経験」を持つかは別問題である。

## Responsible-Agency Program

責任主体研究への応用では、哲学的条件を直接AIへ帰属せず、次の順序を守る。

1. 責任条件を哲学的に同定する。
2. 条件を機能的構成要素へ分解する。
3. 各構成要素にformal candidateを割り当てる。
4. behavioral evidenceと内部因果構造の両方を検証する。
5. 機能的成立から責任帰属へのnormative bridgeを別途論証する。

## Four Revision Levels

```text
Level 1: belief revision
Level 2: generative-model revision
Level 3: preference/value revision
Level 4: reflective self-revision
```

Active inferenceは主に1・2を強く形式化する。[[Reflective Self-Formation]]と[[Open-Ended Revisability]]には3・4およびそれらの通時的沈殿が必要になる。

## Open Questions

- Structural mappingの妥当性を現象学側と計算側でどう検証するか。
- phenomenal consciousnessを欠くAIへphenomenological languageを使えるか。
- functional requirementsを満たすことは責任の必要条件、十分条件、証拠のどれか。
- mechanistic interpretabilityは責任能力評価に必須か。

## Related

- [[Functional Passive Synthesis]]
- [[Precision-Weighted Affection]]
- [[Computational Phenomenology Does Not Establish Moral Responsibility]]
- [[Free Will Conditions for Artificial Moral Responsibility|Conditions for Artificial Responsible Agency]]
