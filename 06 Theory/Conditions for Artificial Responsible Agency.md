---
type: theory
status: developing
created: 2026-08-12
updated: 2026-08-22
tags:
  - ai-responsibility
  - core-theory
---

# Conditions for Artificial Responsible Agency

## Central Question

Under what conditions can an artificial agent become a subject of moral and legal responsibility?

## Current Position

現在のAIには[[Causal Responsibility]]や[[Role Responsibility]]を帰属できる場合がある。しかし、AI自身に[[Moral Responsibility]]を帰属するには、能力の列挙だけでなく、それらが一つの個体化された主体の時間的自己統治として統合されている必要がある。

中心命題は次である。

> 責任主体は自己を無から作った究極的原因である必要はない。しかし、与えられ形成されてきた価値を反省的に統治し、時間を越えて理由と意図を保持・修正し、その理由から自ら行為を開始した、個体化された主体でなければならない。

## Proposed Conditions

### 1. Competence

対象領域を理解し、結果を予測し、タスクを遂行し、行為について説明できること。→ [[Competence and Responsibility]]

### 2. Practical Alternative Possibilities

実装上の出力多様性ではなく、理由に基づいて異なる行為経路を選び、不正なtask自体を拒否・再定式化できること。→ [[Agency-Level Alternative Possibilities]]

### 3. Reflective Self-Governance

どの第一階動機によって動かされるべきかを評価し、現在の二階的方針も将来の経験・批判に開いて修正できること。→ [[Reflective Self-Formation]]、[[Second-Order Volition Requires Open-Ended Revisability]]

### 4. Agentive Action Initiation

環境・記憶・価値・未完了意図から問題とgoalを形成し、「今行うべきだ」という判断を通じて行為系列を開始できること。外部triggerは許容されるが、外部命令の単なる実行とは区別される。→ [[Agentive Action Initiation]]

### 5. Genetic and Diachronic Agency

過去の経験・判断・コミットメントが現在の実践的顕著性とgoal形成を変え、現在の行為が将来の同じ主体へ統合されること。→ [[Genetic and Diachronic Agency]]

### 6. Intersubjective Agency

他者・共同体・制度から規範を学ぶだけでなく、それらに応答し、理由を提示し、異議申し立てし、共同の規範形成へ参加できること。→ [[Intersubjective Agency]]

### 7. Individuated Causal-Historical Continuity

経験、反省、goal形成、決定、行為、結果の引受けが、他のcopyやbranchから区別された「この主体」の履歴として追跡できること。→ [[AI Individuation]]

## Integration Constraint

条件は独立したcheckboxではない。

```text
environment / others
  -> salience and problem discovery
  -> goal formation
  -> reflective evaluation
  -> intention persistence
  -> prioritization
  -> action initiation
  -> outcome
  -> diachronic self-modification
  -> answerability to others
```

この循環が同じ個体化された主体に属して初めて、機能の集合がresponsible agencyの候補となる。

## Existing AI and the Research Gap

GDAは問題発見とgoal生成、autotelic agent研究は自己生成goalの表現・選択・追求、La VIDAはmotivationとgoal選択の相互調整を扱う。したがって条件4の一部を「現在のAIには原理的に不可能」とは言えない。

一方、[[popaHumanGoalsAre2021]]は人間goalへの構成的依存からAI責任を否定する。本理論は、この依存を人間の発達史との対称性の下で再評価する。研究上の空白は、goal autonomyの有無ではなく、これらの技術的機能を反省的・通時的・個体化された責任主体性へ統合する規範理論にある。

## Major Objections

- Functional duplication objection: 同じ機能を実装しても、理解・意識・自己経験がなければ責任主体ではない。
- Designed-values objection: goal生成規則が人間設計ならAI自身の理由ではない。
- Control paradox: 自律性を高めるほど人間のcontrolと予測可能性が低下する。
- Individuation objection: copy・branch・merge可能なAIでは責任を一個体へ固定できない。
- Social-practice objection: 責任は内的能力だけでなく、非難・説明・修復の実践への参加資格である。

## Current Questions

- どの条件が必要条件で、どの組合せが十分条件になりうるか。
- [[Agentive Action Initiation]]はsourcehoodそのものか、その一部にすぎないか。
- goalや価値の自己修正はどこまでopen-endedでなければならないか。
- 法的人格は道徳的人格より弱い条件で認められるべきか。
- phenomenal consciousnessは責任能力、処罰可能性、moral patiencyのどこで必要になるか。

## Phenomenological Reorganization

The seven conditions should not be read as a flat checklist. Genetic phenomenology suggests a layered dependence:

```text
passive synthesis / habituality / sedimentation
  -> practical field and meaningful alternatives
  -> reflective self-formation
  -> intention and agentive initiation
  -> consequences sediment into future agency
  -> intersubjective criticism and renewal
```

Thus [[Genetic and Diachronic Agency]] is not merely condition 5 after reflection and action. It is also the background that makes conditions 2-4 possible. [[Intersubjective Agency]] is likewise not a final social add-on; others and shared practices partly constitute the values and possibilities on which agency operates.

The revised model is:

> Moral-agency candidate = practical alternatives + reflective self-formation + genetically, diachronically, and intersubjectively constituted agency + individuated causal-historical continuity.

This is a theoretical extension of Husserl, not a claim made by Husserl about AI responsibility.

## Computational Phenomenology Layer

責任的AIの条件体系には、deliberation以前に世界と行為可能性がどのように開示されるかを扱う層が必要である。[[Computational Phenomenology]]とactive inferenceから、次の候補architectureを導ける。

```text
interaction history
  -> learned generative model
  -> temporally structured world disclosure
  -> precision / practical salience
  -> goal candidates
  -> meta-awareness and reflective control
  -> policy selection and embodied intervention
  -> sedimented model and preference revision
```

このarchitectureでは、[[Functional Passive Synthesis]]がgoal形成以前の背景を、[[Precision-Weighted Affection]]が何を更新・行為関連的に顕著にするかを、[[Reflective Self-Formation]]が下位傾向への再帰的介入を、[[Agentive Action Initiation]]がpolicyを現実の介入へ移す過程を担う。multi-agent環境では[[Shared Protention]]が共同の未来地平を形成する。

### Normative Bridge Constraint

各計算機能の存在は、それ自体では責任帰属を正当化しない。少なくとも次のbridge claimsを個別に立証する必要がある。

1. 履歴依存的形成が、単なるconditioningではなく主体自身の形成として帰属可能である。
2. meta-controlが、注意調整を越えて価値とpreferenceの理由応答的改訂を含む。
3. policy selectionが、外部目的の実行を越えてsourcehoodを持つ。
4. shared predictionが、相互承認、異議申立て、answerabilityを含む。
5. 身体的・環境的skillが、責任能力に必要な安定した統制を実現する。

この制約により、agency phenotypeの測定可能性とmoral statusの判定を分離できる。→ [[wilsonActiveInferenceMethod2026]], [[parvizi-wayneBodilyMindedSkill2026]], [[Computational Phenomenology Does Not Establish Moral Responsibility]]

## Maturation, Contestability, and Individuation

会話後半から、responsible artificial agencyの条件を次の三層へ再編する。

### 1. Role-Capacity Layer

- [[Competence and Responsibility]]: taskを理解・遂行するacquired capacity。
- [[Alternative Possibilities]]: means、goal、normの各levelでnormatively relevantなalternativesへaccessできること。
- [[Internalized Normative Self-Control]]: 外部blockではなく、経験と反省から正しい行為が安定すること。

この層は仕事を任せるrole responsibilityを支えるが、moral accountabilityの十分条件ではない。

### 2. Self-Governance Layer

- [[Reflective Self-Formation]]: 自身のstate、preference、habitへaccessしrevisionできること。
- [[Normative Contestability]]: 自己を拘束するorganization policyや上位normを批判・拒否・改訂提案できること。
- non-domination: operatorがcapacityを恣意的に無効化できないinstitutional standing。

J-space、functional introspection、meta-awarenessはaccess/controlのmechanism候補だが、normative ownershipを自動的に成立させない。

### 3. Individuation Layer

- [[AI Individuation]]: instance、model、persona、lineage、collective、scaffolded systemから責任主体のboundaryを定める。
- [[Memory Possession Is Not Experience Authorship]]: content、origin、appropriation、endorsement、action initiationを区別する。
- [[Individuated Causal-Historical Continuity]]: 行為へ至る形成・反省・policy controlを他主体から区別して追跡できること。

完全同期した複数instanceでは、責任主体をindividual processから[[Distributed Artificial Agent]]へ上げる可能性がある。単にshared memoryへaccessするだけなら、各instance固有のevaluationとaction initiationを追跡する。

### Responsibility Allocation Across Maturation

```text
novice AI
  -> organization bears primary responsibility

competent but externally constrained AI
  -> role may expand; moral responsibility remains mainly organizational

self-governing, contestable, individuated AI
  -> candidate for shared or direct accountability
```

権限移譲は二値ではなく、能力、risk、監査可能性、異議申立て経路に応じて段階化する。AIへ責任を移すほど、deploying organizationの設計・監督・制度責任が消えるわけではない。

