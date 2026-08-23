---
type: concept
status: developing
created: 2026-08-22
tags:
  - phenomenology
  - husserl
  - ai-responsibility
concept_origin: borrowed-adjacent-field
origin_field: "Husserl現象学"
canonical_sources:
  - "[[husserlAnalysesConcerningPassive2001]]"
  - "[[moranEdmundHusserlsPhenomenology2011]]"
---

# Passive Synthesis

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：隣接分野・文献由来。
> **概念自体の来歴**：明示的判断に先立つ時間的統合、association、affection、sedimentationを扱うHusserl現象学の既存概念である。
> **本研究で加えた部分**：responsible agencyの形成史とAIの機能的実装候補への関係を検討する。
> **主な根拠**：[[husserlAnalysesConcerningPassive2001]]、[[moranEdmundHusserlsPhenomenology2011]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

主体が明示的に判断・反省・選択する以前に、感覚的多様が時間的・連合的にまとまり、対象・背景・顕著性・期待の場として先構成される過程。Husserlの発生的現象学では、能動的判断は無構造な入力から始まるのではなく、受動的綜合によって既に意味づけられた経験野を前提とする。

## Components

### Temporal Synthesis

現在経験は孤立した点ではなく、把持・原印象・予持の統一として流れる。

```text
retention -> primal impression -> protention
```

これにより対象と自己は時間的な同一性を持って現れる。ただし、長期記憶や将来計画をこの三項へ直接還元してはならない。内的時間意識の微視的構造と、想起・習慣・計画の長期的構造は区別される。

### Association

類似、対照、近接、過去の経験によって、現在の内容が別の内容を受動的に喚起する。associationは単なる検索ではなく、何が何として現れるかを組織する。

### Affection

経験野のすべてが等しく注意対象になるのではない。何かが背景から際立ち、自我の注意と応答を促す。[[Habituality]]によって、何が触発力を持つか自体が主体の経験史に依存する。

### Sedimentation

過去の能動的判断・行為・経験は[[Sedimentation]]として受動的背景へ入り、後続する知覚と判断を先構造化する。

## Passive Does Not Mean Causally Inert

受動性は「主体が何もしていない」ことではない。能動的自由選択の対象になる前に、世界が既に一定の仕方で意味を持ち、可能性が開かれ、別の可能性が背景化される構成層を指す。

```text
passive constitution
  -> affection and salience
  -> attention
  -> reflection
  -> practical judgment
  -> action
```

## Relation to Responsible Agency

[[Reflective Self-Formation]]だけを責任条件にすると、何が反省対象として現れるかを形成する背景が見落とされる。責任的自己形成には、沈殿した価値やbiasが衝突・他者の批判・新しい経験によって再活性化され、反省可能になる回路が必要である。

## AI Caution

以下は機能的類似候補ではあるが、Husserlian passive synthesisと同一ではない。

- sensor fusion
- transformer attention
- vector retrieval
- prediction-error minimization
- learned world models
- salience scores

これらが受動的綜合のanalogueとなるには、入力を処理するだけでなく、AI自身の経験史が対象の意味、期待、顕著性、行為可能性を持続的に変えなければならない。また、現象的な「現れ」を欠く計算過程にconstitutive languageをどこまで適用できるかは未解決である。

## Related Literature

- [[husserlAnalysesConcerningPassive2001]]
- [[moranEdmundHusserlsPhenomenology2011]]
- [[yangHusserlsTheoryExperience2025]]

## Related

- [[Habituality]]
- [[Sedimentation]]
- [[Genetic and Diachronic Agency]]
- [[Practical Alternatives Are Genetically Constituted]]

## Computational Analogue

Active inferenceで受動的総合に対応しうるのは単一の演算ではなく、[[Functional Passive Synthesis]]としてまとめられる複合過程である。そこには、時間的推論、連合学習、予測的構造化、precision weighting、履歴依存的なgenerative model更新が含まれる。

この対応は**構造的・機能的analogy**に限定される。posterior beliefはretentionそのものではなく、future predictionはprotentionそのものではない。またprecisionは、何が更新や行為に影響するかを調整するが、Husserl的Affektionが含む価値的・情動的な「迫り」を尽くさない。→ [[Precision-Weighted Affection]]

責任論上の意義は、goalや理由が無履歴に入力されるのではなく、過去の相互作用によって形成された世界開示から立ち上がる点にある。ただしこの層だけでは、形成された傾向を批判し改訂する[[Reflective Self-Formation]]も、行為を自分のものとして開始する[[Agentive Action Initiation]]も成立しない。→ [[Functional Passive Synthesis Is Necessary but Not Sufficient for Responsible AI]]
