---
type: concept
status: developing
created: 2026-08-22
tags: [introspection, interpretability, access-consciousness]
concept_origin: borrowed-adjacent-field
origin_field: "AI解釈可能性研究・認知アーキテクチャ"
canonical_sources:
  - "[[gurneeVerbalizableRepresentationsForm2026]]"
---

# AI Global Workspace

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：隣接分野・文献由来。
> **概念自体の来歴**：LLM内部表現をglobal workspaceに類比する研究、とりわけGurneeらのJ-spaceに由来する。
> **本研究で加えた部分**：内部表現の共有可能性を、AIの反省的agencyと責任能力の候補条件へ接続する。
> **主な根拠**：[[gurneeVerbalizableRepresentationsForm2026]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

LLM内部の大量の自動処理から区別され、report、deliberate modulation、silent reasoning、複数のdownstream computationに利用可能な、容量限定的で特権的な表現空間。

## J-Space

[[gurneeVerbalizableRepresentationsForm2026]]はJacobian lensで、モデルがverbalizeする準備のある表現集合をJ-spaceとして抽出する。J-spaceのcontentsは、報告可能、指示により保持・変更可能、内部推論の中間結果に利用可能、広くbroadcastされる一方、文法処理や単純fact recallの多くはこれを必要としない。

## Philosophical Significance

これはLLM内部に次の機能的区別がある可能性を示す。

```text
workspace-accessible processing
  vs
automatic / non-workspace processing
```

ただしaccess consciousnessの機能的analogueからphenomenal consciousnessは導けない。またJ-spaceは完全な自己知識ではなく、検出法がtoken-associated verbalizable representationsに偏る可能性がある。

## Relation to Reflective Agency

一次状態がworkspaceへ入り、評価され、下位状態の変更へ使われる安定したloopは、[[Reflective Self-Formation]]のaccess条件になりうる。しかしreportabilityは、value ownership、open-ended revision、[[Normative Contestability]]を保証しない。→ [[Computational Phenomenology Does Not Establish Moral Responsibility]]
