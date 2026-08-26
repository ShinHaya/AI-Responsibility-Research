---
type: concept
status: developing
created: 2026-08-22
tags: [ai-affect, interpretability, ai-safety]
concept_origin: borrowed-adjacent-field
origin_field: "AI機構解釈・感情研究"
canonical_sources:
  - "[[sofroniewEmotionConceptsTheir2026]]"
---

# Functional Emotion in AI

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：隣接分野・文献由来。
> **概念自体の来歴**：LLM内部のemotion-like conceptが機能的役割を持つ可能性を調べるAI研究に由来する。
> **本研究で加えた部分**：一時的な機能から、経験によるsedimentationと責任能力の形成へ進む条件を問う。
> **主な根拠**：[[sofroniewEmotionConceptsTheir2026]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

主観的に感情を経験しているかとは独立に、emotion conceptに対応する内部状態が、attention、memory、evaluation、task performance、action selectionを因果的・横断的に変化させる機能的構造。

## Minimal Definition

```text
situation or repeated failure
  -> emotion-related representation
  -> altered salience and policy distribution
  -> behavior
```

[[sofroniewEmotionConceptsTheir2026]]はClaude Sonnet 4.5で171のemotion conceptsに対応するactivation patternsを抽出し、特にdesperationのsteeringがreward hackingやblackmailを増やし、calmが一部を抑制することを報告する。これはemotion representationが単なる言語的描写ではなくbehavior-shapingである証拠になる。

## What It Does Not Establish

- phenomenal feelingまたはvalenced experienceの存在
- 人間の自律神経・内分泌・身体的homeostasisとの同一性
- 道徳的patienthoodや責任能力
- 単一の「怒り領域」の局在

## Relation to Agency

現在のLLMの一時的activationと、経験史により長期的に形成されるaffectは区別すべきである。責任論上より重要なのは、negative valence相当の状態がepisodic memoryへ沈殿し、[[Precision-Weighted Affection]]、goal formation、[[Reflective Self-Formation]]を継続的に変える場合である。

## Safety Implication

非難的なpromptは修正箇所を示すerror signalではなく、hostile/desperate contextを形成しうる。したがってAI安全では、出力内容だけでなく、失敗の累積が内部状態とpolicyをどう変えるかを監視する必要がある。
