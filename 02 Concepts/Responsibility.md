---
type: concept
status: developing
created: 2026-08-12
tags:
  - ai-responsibility
concept_origin: established-analytic-free-will
origin_field: "倫理学・法哲学・道徳的責任論"
canonical_sources:
  - "[[shoemakerAttributabilityAnswerabilityAccountability2011]]"
  - "[[matthiasResponsibilityGap2004]]"
---

# Responsibility

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：分析哲学の標準概念。
> **概念自体の来歴**：因果的、役割上、道徳的、法的責任を区別する責任論の既存語彙をまとめた上位概念である。
> **本研究で加えた部分**：AIについて各責任類型の成立条件と、上位責任判断に必要な証拠基盤を分離して整理する。
> **主な根拠**：[[shoemakerAttributabilityAnswerabilityAccountability2011]]、[[matthiasResponsibilityGap2004]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

AIへの責任帰属では、少なくとも以下を区別する必要がある。

## Causal Responsibility

AIの判断・行為が、ある結果を因果的に生じさせたという意味での責任。

現在のAIにも帰属可能である。

## Role Responsibility

ある役割やタスクをAIに割り当て、その役割上の義務を果たすことを期待するという意味での責任。

これも現在のAIに機能的に帰属可能である。

## Moral Responsibility

行為について賞賛・非難される主体であるという意味での責任。

現在のAIに帰属できるかは疑わしい。

## Legal Responsibility

法的義務・制裁等の独立した帰属主体となること。

現在のAIへの帰属には大きな問題がある。

## Current Position

AIに[[Responsibility#Causal Responsibility|Causal Responsibility]]と[[Responsibility#Role Responsibility|Role Responsibility]]を帰属することと、[[Responsibility#Moral Responsibility|Moral Responsibility]]・[[Responsibility#Legal Responsibility|Legal Responsibility]]を帰属することを区別する。

後二者には、単なる因果能力やタスク遂行能力以上の主体性が要求される。

## Epistemic Preconditions

責任の種類と、責任帰属を可能にする証拠条件を区別する必要がある。

agent identity、委任関係、因果系列を追跡できなければ、どの主体のどの役割違反を評価すべきか確定できない。

したがって[[Agentic Causal Provenance]]は責任そのものではないが、上位の責任判断を可能にする認識的基盤となる。

→ [[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]

## Explanation Generation and Accountability

AIがprovenanceから説明文を生成する能力と、説明責任を負う主体であることを区別する必要がある。

```text
evidence production
  → AI-assisted explanation
  → human or institutional review
  → responsibility judgment and remedy
```

説明を生成できることだけでは、AIに法的または道徳的責任があることを示さない。

AIへ課しうるのは、委任された業務の経過と根拠を報告するrole-defined dutyである。

その説明の妥当性を検証し、責任を判断し、被害を救済するaccountabilityは人間と組織に残る。

→ [[Corporate Remedial Responsibility for Agentic AI]]

## Related

- [[Alternative Possibilities]]
- [[Reflective Self-Formation]]
- [[Genetic and Diachronic Agency]]
- [[AI Individuation]]
- [[Agentic Causal Provenance]]
- [[Free Will Conditions for Artificial Moral Responsibility|Conditions for Artificial Responsible Agency]]
