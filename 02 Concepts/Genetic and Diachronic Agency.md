---
type: concept
status: developing
created: 2026-08-12
updated: 2026-08-22
tags:
  - phenomenology
  - ai-responsibility
  - agency
concept_origin: project-extension
origin_field: "Husserl現象学・planning agency・人格同一性"
canonical_sources:
  - "[[husserlAnalysesConcerningPassive2001]]"
  - "[[moranEdmundHusserlsPhenomenology2011]]"
  - "[[bratmanPlanningAgencyAutonomous2005]]"
---

# Genetic and Diachronic Agency

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究による再構成。
> **概念自体の来歴**：genetic phenomenology、planning agency、時間を越えた自己統治に関する既存理論を基礎とする。
> **本研究で加えた部分**：経験が価値、習慣、注意、goal形成を変え、その変化を同一主体が反省的に引き受ける統合条件として再構成する。
> **主な根拠**：[[husserlAnalysesConcerningPassive2001]]、[[moranEdmundHusserlsPhenomenology2011]]、[[bratmanPlanningAgencyAutonomous2005]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

主体が現在瞬間の能力集合ではなく、過去の経験・判断・コミットメントを保持し、それらによって将来の知覚、顕著性、価値判断、目標形成、行為を変化させ続ける時間的プロセスであること。

## Core Structure

```text
experience(t0)
  -> intention / commitment
  -> persistence and sedimentation
  -> changed salience and practical outlook
  -> recall and prioritization(t1)
  -> action
  -> outcome and self-modification(t2)
```

通時性は単なる時系列的連続ではない。過去の理由を現在の行為理由として引き受け、現在の選択を将来の自己に拘束力を持つコミットメントとして形成できることが重要である。

## Planning and Prospective Agency

[[bratmanPlanningAgencyAutonomous2005]]が扱うplanning agencyは、将来志向的な意図と計画が活動を時間横断的に組織する点を示す。[[pacherieAgency2026]]は、計画保持だけでなく、意図が適切な時点で行為制御へ接続されるagencyの階層を考えるための補助線となる。

この観点では、ToDoデータベースを持つことと、展望的な主体であることは異なる。保存された項目が、同じ主体の未完了意図として再活性化され、現在の理由・価値・状況との比較を経て行為を開始させなければならない。

## Memory Database vs Diachronic Transformation

```text
memory database:
past -> stored record -> retrieval

diachronic agency:
past experience -> transformed agent -> changed future perception and action
```

AIが過去ログを検索できても、その経験が何を重要と感じ、どのgoalを形成し、どの理由を自分の理由として扱うかを変えないなら、強い意味での経験史は形成されていない。

## Relation to Agentive Initiation

[[Agentive Action Initiation]]が一時点での行為の起点を扱うのに対し、本概念は、その起点が過去の同じ主体の経験と将来の同じ主体へのコミットメントに接続されることを要求する。

```text
initiation without diachrony = isolated autonomous episode
diachrony without initiation = persistent planner that never becomes an actor
```

責任主体には両方が必要である。

## AI Individuation Problem

AIは状態・memory・policyをcopy、branch、merge、synchronizeできる。したがって、同じ記憶内容を持つことは同じ経験主体であることを意味しない。問うべきなのは、どの因果的・実践的履歴が当該行為へ連続しているかである。

## Open Questions

- goal生成とpriority更新だけで通時的主体性を認められるか。
- 過去の意図を現在の理由として「引き受ける」ために現象的意識は必要か。
- branch前のコミットメントは、branch後のどの個体を拘束するか。
- 他者・組織・文化から得た規範を自己の理由へ変換するには[[Intersubjective Agency]]が必要か。

## Related

- [[Agentive Action Initiation]]
- [[Reflective Self-Formation]]
- [[AI Individuation]]
- [[Memory Possession Is Not Experience Authorship]]
- [[Free Will Conditions for Artificial Moral Responsibility|Conditions for Artificial Responsible Agency]]

## Phenomenological Foundation

[[Passive Synthesis]] explains how a meaningful experiential field is formed before explicit reflection. [[Habituality]] explains how past experience becomes a durable perceptual and practical style. [[Sedimentation]] explains how active achievements become the passive background of later agency.

This revises diachronic agency from mere temporal persistence into a genetic cycle:

```text
world and others
  -> passive synthesis and affection
  -> meaningful practical possibilities
  -> reflection and action
  -> sedimentation and habituality
  -> transformed future subject
```

The cycle is open rather than closed: world and others continually affect the subject, while the subject carries a historically formed horizon into each encounter. See [[Genetically and Intersubjectively Constituted Agency Is Required for AI Responsibility]].
