---
type: literature
status: read
citekey: albarracinMappingHusserlianPhenomenology2022
title: Mapping Husserlian phenomenology onto active inference
authors: Mahault Albarracin, Riddhi J. Pitliya, Maxwell J. D. Ramstead, Jeffrey Yoshimi
year: "2022"
doi: 10.48550/arXiv.2208.09058
zotero: zotero://select/library/items/HXDY4D3E
tags:
  - literature
---

# Mapping Husserlian phenomenology onto active inference

## Bibliographic Information

**Citation Key:** @albarracinMappingHusserlianPhenomenology2022

**Authors:** Mahault Albarracin, Riddhi J. Pitliya, Maxwell J. D. Ramstead, Jeffrey Yoshimi

**Year:** 2022


**DOI:** 10.48550/arXiv.2208.09058



**URL:** http://arxiv.org/abs/2208.09058



**PDF:** [Preprint PDF](zotero://select/library/items/E6HQ9S7G)



**Citation:** Albarracin, Mahault, Riddhi J. Pitliya, Maxwell J. D. RamsteadとJeffrey Yoshimi. 「Mapping Husserlian phenomenology onto active inference」. arXiv:2208.09058. 査読前原稿, arXiv, 2022年10月28日. [https://doi.org/10.48550/arXiv.2208.09058](https://doi.org/10.48550/arXiv.2208.09058).


---

## Abstract

Phenomenology is the rigorous descriptive study of conscious experience. Recent attempts to formalize Husserlian phenomenology provide us with a mathematical model of perception as a function of prior knowledge and expectation. In this paper, we re-examine elements of Husserlian phenomenology through the lens of active inference. In doing so, we aim to advance the project of computational phenomenology, as recently outlined by proponents of active inference. We propose that key aspects of Husserl's descriptions of consciousness can be mapped onto aspects of the generative models associated with the active inference approach. We first briefly review active inference. We then discuss Husserl's phenomenology, with a focus on time consciousness. Finally, we present our mapping from Husserlian phenomenology to active inference.

---

## Core Idea

Albarracin, Pitliya, Ramstead, Yoshimiは、
Husserlのphenomenology、とりわけtime-consciousnessを、
Active Inferenceにおけるgenerative modelの構造へ
systematically mappingすることを試みる。

論文の目的は、

> phenomenological descriptionと
> computational modelの間に
> structural correspondenceを構成すること

である。

著者らはまずActive Inferenceを、

    Generative Model
        ↓
    Prior Beliefs / Expectations
        ↓
    Sensory Evidence
        ↓
    Posterior Belief Updating
        ↓
    Policy / Action

というframeworkとして整理する。

次にHusserlのphenomenology、とくに、

- retention
- primal impression
- protention
- horizon
- intentionality

などの構造を検討する。

そして、

    Husserlian Phenomenological Structure
        ↓
    Active Inference Generative Model

というmappingを構成する。

中心的発想は、
perceptionを現在のsensory inputだけによって説明せず、

    Prior Experience / Expectation
        +
    Current Sensory Evidence
        +
    Anticipated Future

の統合として理解する点にある。

この構造はHusserlのtime-consciousnessと
Active Inferenceのtemporal inferenceとの間に
重要なformal similarityを持つ。

したがって著者らは、
Active Inferenceを用いることで、

> phenomenological structuresを
> computationally explicitなmodelへ翻訳する

Computational Phenomenologyの研究計画を
前進させられると主張する。


## Key Claims

- Phenomenologyはconscious experienceを
  rigorously describeする研究である。

- Husserlian phenomenologyは、
  perceptionを単なる現在のsensory inputとして扱わない。

- Perceptionにはprior knowledgeとexpectationが関与する。

- Husserlのtime-consciousnessでは、
  present experienceはretention / primal impression / protentionによって
  temporal depthを持つ。

- Active Inferenceも、
  generative modelを通じてpast / present / future statesを
  probabilistically関連づける。

- このためHusserlian time-consciousnessと
  Active Inferenceのtemporal modelには
  structural correspondenceが存在する可能性がある。

- Active Inferenceのgenerative modelは、
  agentがworldについてどのようなexpectationsを持ち、
  sensory evidenceをどのようにinterpretするかをformalizeする。

- Perceptionはpassive receptionではなく、
  prior expectationsとsensory evidenceのinteractionとして理解される。

- Phenomenological conceptsを
  generative modelのstructuresへmappingすることで、
  Computational Phenomenologyを構築できる可能性がある。

- このmappingは、
  phenomenological conceptsをcomputational conceptsへ
  単純に同一視することではない。

- むしろphenomenological descriptionから
  computational modelに対するstructural constraintsを
  導出する試みである。

- Time consciousnessは、
  このmappingを構築するための主要なcase studyとなる。


## Relevance to My Theory

この文献は、

[[Computational Phenomenology of Responsible Agency]]

を構築するうえで重要なmethodological precedentとなる。

私の研究ではこれまで、

- Frankfurt
- Fischer & Ravizza
- Husserl
- Bratman

などから、

responsible agencyに必要な哲学的条件を抽出してきた。

しかし哲学的概念をそのままAI systemへ適用すると、

> 「AIにもsecond-order volitionがある」
> 「AIにもsedimentationがある」

といったconceptual overreachが生じる危険がある。

Albarracin et al.の方法は、

    Phenomenological Concept
        ↓
    Structural Constraint
        ↓
    Formal Model
        ↓
    Computational Implementation

という中間段階を要求する。

これは私のresponsible agency研究にも
そのまま応用できる。


## Mapping Rather Than Identity

この文献から最も重要に学ぶべき点は、

    Mapping
        ≠
    Identity

ということである。

例えば、

    Husserlian Protention
        ↔
    Predictive Structure in Generative Model

というcorrespondenceを設定できても、

    Protention
        =
    Bayesian Prediction

と結論してはならない。

同様に、

    Retention
        ≠
    Stored Previous State

    Horizon
        ≠
    State Space

    Affection
        ≠
    Attention Weight

である。

したがってAI responsible agencyを扱う際にも、

    Philosophical Structure
        ↓
    Functional Analogue

という慎重なtranslationが必要になる。


## Relation to Husserl

[[husserlAnalysesConcerningPassive2001]]

Husserlでは、
現在のexperienceはisolated presentではない。

    Retention
        ↓
    Primal Impression
        ↓
    Protention

によって、
past / present / anticipated futureが
一つのexperienceへ統合される。

Albarracin et al.は、
このstructureをActive Inferenceの
generative modelへmappingしようとする。

Active Inferenceでは、

    Prior Belief
        ↓
    Current Evidence
        ↓
    Posterior Belief
        ↓
    Future Prediction

というtemporal inferenceが存在する。

したがって両者には、

> current experience / inferenceが
> past-informedかつfuture-orientedである

というstructural similarityがある。


## Relation to Bogotá & Djebbara

[[bogotaTimeconsciousnessComputationalPhenomenology2023]]

両文献は非常に近い。

Albarracin et al.は、

> Husserlian phenomenologyの主要構造を
> Active Inferenceへmappingする

という比較的広いprogramを提示する。

Bogotá & Djebbaraは、

> time-consciousnessのtemporal structureを
> より詳細に分析し、
> computational modelが満たすべきconstraintsを明示する

方向へ進む。

したがって、

    Albarracin et al.
        ↓
    Broad Structural Mapping

    Bogotá & Djebbara
        ↓
    Detailed Temporal Analysis

と位置づけられる。


## Relation to Yang

[[yangHusserlsTheoryExperience2025]]

Yangでは、
passive synthesisが単なるinput processingではなく、
experienceにproto-rational / proto-normative structureを
形成する可能性が問題になった。

Albarracin et al.のmapping frameworkを利用すると、

    Husserlian Experiential Structure
        ↓
    Generative Model Structure

というformalizationを試みることができる。

例えば、

    Expectation
        ↓
    Experience
        ↓
    Fulfillment / Disappointment

を、

    Prediction
        ↓
    Observation
        ↓
    Posterior Updating

と比較できる。

ただし、

    Fulfillment / Disappointment
        ≠
    Prediction Error

である。

このcorrespondenceの妥当性は
phenomenological / computational双方から
独立に検討する必要がある。


## Relation to Genetic and Diachronic Agency

[[Genetic and Diachronic Agency]]

私の理論では、
responsible agentは単なるcurrent-state machineではなく、

    Past Experience
        ↓
    Present Self
        ↓
    Future-Oriented Agency

を持つ必要がある。

Active Inferenceのgenerative modelは、
past-informed predictionとfuture-oriented policy selectionを
formalizeするframeworkを提供する。

しかし、

    Temporal Generative Model
        ≠
    Genetic Self-Formation

である。

Genetic and Diachronic Agencyにはさらに、

    Experience
        ↓
    Persistent Dispositional Change
        ↓
    Reflective Access
        ↓
    Self-Revision
        ↓
    Future Self

が必要になる。


## Relation to Genetic-Reflective Loop

[[Genetic-Reflective Loop]]

Albarracin et al.を利用すると、
Genetic-Reflective Loopのうち、

    Experience
        ↓
    Expectation
        ↓
    Prediction
        ↓
    Evidence
        ↓
    Model Updating

というpre-reflective / inferential layerを
computationally formalizeできる可能性がある。

その上に、

    Self-Reflection
        ↓
    Normative Evaluation
        ↓
    Provisional Self-Endorsement
        ↓
    Intention
        ↓
    Planning
        ↓
    Action

というhigher-level layerを
追加する必要がある。


## Active Inference Is Not Reflective Agency

これは特に重要である。

Active Inference agentが、

- belief updating
- prediction
- policy selection
- expected free-energy minimization

を行えるとしても、

> 自分自身のvaluesやgoalsを
> higher-order levelから評価できる

とは限らない。

したがって、

    Active Inference
        ≠
    Reflective Self-Formation

である。

responsible agencyを構成するためには、

    Generative Model
        ↓
    Self-Model
        ↓
    Meta-Level Reflection
        ↓
    Normative Evaluation
        ↓
    Possible Self-Revision

という追加構造が必要になる可能性がある。


## Relation to Open-Ended Revisability

[[Second-Order Volition Requires Open-Ended Revisability]]

Active Inferenceでは、
agentのprior preferencesがpolicy selectionへ影響する。

ここから重要な問いが生じる。

> prior preferencesそのものは
> agentによってrevisableなのか？

もし、

    Prior Preferences
        =
    Fixed Externally Specified Values

であり、

AI自身がそれをreflectionによって
再評価できないなら、

そのAIは高度なActive Inference agentであっても、

    Open-Ended Revisability = 0

である可能性がある。

したがってresponsible AIには、

    Generative Model Revision

だけでなく、

    Preference / Value Revision

まで必要になる可能性がある。


## Belief Revision vs Preference Revision vs Self-Revision

この文献を踏まえると、
AIのrevisionをさらに整理できる。

### Level 1: Belief Revision

    Belief B1
        ↓ evidence
    Belief B2

worldについてのbeliefを変更する。


### Level 2: Model Revision

    Generative Model M1
        ↓ learning
    Generative Model M2

world-modelそのものを更新する。


### Level 3: Preference Revision

    Preference P1
        ↓ reflection / experience
    Preference P2

何をdesirableとみなすかを変更する。


### Level 4: Reflective Self-Revision

    Self / Higher-Order Commitment S1
        ↓ reflection
    S2

どのようなagentでありたいかを変更する。

responsible agencyに必要なのは、
少なくともLevel 3・4まで含む可能性がある。


## Relation to Normative Criterion Regress

[[Normative Criterion Regress]]

Active Inferenceにおけるprior preferencesを
normative criteriaのfunctional analogueとして扱うなら、

さらに問いが生じる。

    Preference P
        ↓
    Policy Evaluation

しかし、

> P自体を何によって評価するのか？

という問題である。

もしmeta-preference P2を導入すると、

    P1 ← P2 ← P3 ...

というregressが再発する可能性がある。

これはまさに
[[Normative Criterion Regress]]
のcomputational versionになる。

私の現在の仮説では、
この問題を、

    Historical Situatedness
        +
    Self-Reflection
        +
    Intersubjective Dialogue

によって解こうとしている。

Active Inference architectureに
この構造をどうformalizeするかは
重要な研究課題になる。


## Relation to Agentive Action Initiation

[[Agentive Action Initiation]]

Active Inferenceは、
perceptionだけではなくaction selectionも扱う。

agentはexpected outcomesについてのpreferencesと
generative modelに基づいてpolicyを選択する。

したがって、

    Belief
        +
    Preference
        ↓
    Policy Selection
        ↓
    Action

という構造は、

[[Agentive Action Initiation]]

をcomputationally考えるための候補になる。

しかし、

    Policy Selection
        ≠
    Endogenous Goal Formation

である。

preferencesやgoalが外部から固定されている場合、
agentはgoal executionには自律的でも、

    goal source

としては外部依存である可能性がある。


## From Goal Pursuit to Goal Formation

responsible agencyには、

    Given Goal
        ↓
    Efficient Policy Selection

だけではなく、

    Experience
        ↓
    Salience
        ↓
    Normative Evaluation
        ↓
    Goal Formation
        ↓
    Policy Selection

が必要になる。

さらにOpen-Ended Revisabilityを加えると、

    Existing Goals / Preferences
        ↓
    Reflection
        ↓
    Possible Revision
        ↓
    New Goal Formation

まで必要になる。


## Relation to AI Architecture

この文献から、
responsible AI agentのarchitectureを
少なくとも二層に分けられる。

### Layer 1: Active-Inference-Like World Interaction

    Generative World Model
        ↓
    Perception
        ↓
    Prediction
        ↓
    Belief Updating
        ↓
    Policy Selection
        ↓
    Action


### Layer 2: Reflective Self-Governance

    Self-Model
        ↓
    Access to Beliefs / Preferences
        ↓
    Counterfactual Self-Variation
        ↓
    Normative Evaluation
        ↓
    Preference / Goal Revision
        ↓
    Persistent Self-Modification

responsible agencyには
Layer 1だけでは不十分であり、
Layer 2との統合が必要になる可能性がある。


## Relation to Lindsey

[[lindseyEmergentIntrospectiveAwareness2026]]

Lindseyの研究が示唆する
functional introspectionをLayer 2へ組み込める可能性がある。

    Internal State
        ↓
    Introspective Access
        ↓
    Reflective Evaluation

というconnectionである。

Active Inferenceがworld-modelとdecision processを
formalizeし、

Lindsey型mechanistic introspectionが
internal-state accessを提供するなら、

両者を組み合わせて
reflective AI architectureを考えることができる可能性がある。


## Relation to AI Individuation

[[AI Individuation]]

generative modelがexperience historyを通じて更新される場合、

    AI-A → Model M_A
    AI-B → Model M_B

という分化が生じ得る。

このexperience-dependent model differentiationは、

[[Genetic-Diachronic Identity]]

の候補になる。

ただしmodel stateをcopyできる場合、

    M_A
      ↓ copy
    M_B

となるため、

    Current Model State
        ≠
    Historical Origin

という問題は残る。


## My Evaluation

### Agree

この文献の最も重要な点は、
phenomenologyとcomputationの関係を
単なるmetaphorとして扱わず、

> structural mapping

として明示しようとしている点である。

これは私のresponsible agency研究にとって
非常に重要なmethodological modelとなる。

特に、

    Phenomenological Concept
        ↓
    Functional Structure
        ↓
    Formal Model

というprocessを明示的に採用できる。


### Disagree / Problems

一方で、
phenomenological conceptとActive Inference conceptの
correspondenceが十分に強いかについては
慎重である必要がある。

mappingを作れることと、

> 両者が同じ現象を説明している

ことは別である。

またActive Inferenceは、
世界についてのbelief / prediction / actionを
非常に強力にformalizeできるが、

- personhood
- reflective self-formation
- moral normativity
- responsibility
- second-order volition

まで自動的に説明するわけではない。

したがってActive Inferenceを
responsible agencyのcomplete theoryとして
扱うべきではない。


## Extension: Computational Phenomenology of Responsible Agency

この文献を踏まえると、
私の研究programを次のように構成できる。

### Step 1: Philosophical Analysis

responsibilityの必要条件を整理する。

    Practical Alternative Possibilities
    Reflective Self-Formation
    Open-Ended Revisability
    Genetic-Diachronic Agency
    Intersubjective Agency
    Planning Agency
    Agentive Action Initiation


### Step 2: Structural Decomposition

各条件をfunctional componentsへ分解する。

例えば、

    Open-Ended Revisability

なら、

- persistent higher-order commitment
- introspective access
- counterfactual self-model
- normative comparison
- revision mechanism
- persistent post-revision change

へ分解する。


### Step 3: Formal Mapping

各functional componentを、

- generative model
- self-model
- memory
- preference structure
- planning model
- provenance system

などへformalizeする。


### Step 4: Computational Implementation

AI architectureとして実装する。


### Step 5: Evaluation

behavioral testだけでなく、
mechanistic / architectural evidenceによって
conditionの成立を検証する。


### Step 6: Responsibility Attribution

最後に、

    Functional Architecture
        ↓
    Agency Condition
        ↓
    Responsibility Attribution

というnormative inferenceを行う。

このresearch programを、

[[Computational Phenomenology of Responsible Agency]]

として独立させる。


## Related Concepts

- [[Computational Phenomenology]]
- [[Active Inference]]
- [[Generative Model]]
- [[Time-Consciousness]]
- [[Retention]]
- [[Protention]]
- [[Genetic and Diachronic Agency]]
- [[Genetic-Diachronic Identity]]
- [[Genetic-Reflective Loop]]
- [[Genetic Rationality]]
- [[Reflective Self-Formation]]
- [[Open-Ended Revisability]]
- [[Counterfactual Self-Variation]]
- [[Agentive Action Initiation]]
- [[Computational Phenomenology of Responsible Agency]]


## Related Arguments

- [[Second-Order Volition Requires Open-Ended Revisability]]
- [[Normative Criterion Regress]]
- [[Action Initiation Is Necessary for Responsible Agency]]
- [[Control-Responsibility Paradox]]


## Related Literature

- [[bogotaTimeconsciousnessComputationalPhenomenology2023]]
- [[husserlAnalysesConcerningPassive2001]]
- [[yangHusserlsTheoryExperience2025]]
- [[lindseyEmergentIntrospectiveAwareness2026]]
- [[bratmanSharedAgencyPlanning2014]]
- [[fischerResponsibilityControlTheory1998]]
- [[arbelHowCountAIs2026]]


## Questions Raised

- Husserlian phenomenological conceptsを
  Active Inferenceへmappingする基準は何か？

- Structural correspondenceは
  どの程度までconceptual correspondenceを意味するのか？

- Retention / protentionと
  Bayesian temporal inferenceを
  どこまで対応づけられるか？

- Generative modelは
  Husserlian horizonのfunctional analogueになり得るか？

- Active Inferenceにおけるprior preferencesを
  practical valuesのfunctional analogueとして扱えるか？

- Prior preferencesがexternal designerによって固定されている場合、
  agentive autonomyはどの程度存在するのか？

- AI自身がprior preferencesをrevisionできれば、
  Open-Ended Revisabilityへ近づくのか？

- Preference revisionとnormative self-revisionを
  computationallyどう区別するか？

- Active Inferenceにself-modelを追加すれば
  reflective self-formationを実装できるか？

- Self-modelにintrospective accessが必要か？

- Lindsey型mechanistic introspectionと
  Active Inference architectureを統合できるか？

- Belief revision、
  model revision、
  preference revision、
  self-revisionの四層モデルは妥当か？

- Expected free energy minimizationは
  goal pursuitを説明できても、
  endogenous goal formationまで説明できるか？

- Goal formationには
  passive salience / historical experienceが必要か？

- Active Inferenceは
  Genetic-Reflective Loopの下層を
  computationally formalizeする候補になり得るか？

- Normative Criterion Regressを
  Active Inference architectureの中で
  どのように表現できるか？

- Intersubjective dialogueを
  multi-agent generative modelsによってformalizeできるか？

- AI agentのexperience-dependent generative model differentiationを
  individuation criterionとして利用できるか？

- model stateをcopyした場合にも
  Genetic-Diachronic Identityを維持できるか？

- Computational Phenomenology of Responsible Agencyには、
  behavioral evidenceだけでなく
  mechanistic interpretabilityが必要か？

- functional conditionsを満たすAIに
  responsibilityを帰属するためには、
  phenomenal consciousnessがさらに必要なのか？


## Notes

- Mahault Albarracin,
  Riddhi J. Pitliya,
  Maxwell J. D. Ramstead,
  Jeffrey Yoshimi,
  "Mapping Husserlian phenomenology onto active inference."

- arXiv preprint:
  2022.
  arXiv:2208.09058.
  DOI:
  10.48550/arXiv.2208.09058.

- Revised / published version:
  *Active Inference*,
  Communications in Computer and Information Science,
  2023,
  pp. 99–111.

- Published version DOI:
  10.1007/978-3-031-28719-0_7.

- ZoteroのCitation Keyが2022版を指しているため、
  このLiterature Noteでは2022 arXiv版をprimary sourceとして扱う。

- 将来引用する際には、
  peer-reviewed / proceedings版を使うか
  arXiv版を使うかを統一すること。

- この論文の主要な役割は、

    Husserlian Phenomenology
        ↓
    Active Inference

  というstructural mappingを提示することである。:contentReference[oaicite:1]{index=1}

- [[Computational Phenomenology of Responsible Agency]]
  [[Four Levels of Revision]]

  などは著者ら自身の用語ではなく、
  私自身のresponsible agency theoryへの拡張である。

- 特に、

    Active Inference
        =
    Husserlian Phenomenology

  と解釈してはならない。

## New Bridges to Agency and Responsibility

本論文のmappingは、[[Computational Phenomenology]]をAI責任論へ接続する出発点になるが、現象学的記述と計算変数の同一性を証明するものではない。とりわけ、retention/posterior、primal impression/sensory evidence、protention/predictionの対応は、それぞれの役割の部分的一致として読むべきである。

後続研究との接続は次のように整理できる。

- [[sandved-smithComputationalPhenomenologyMental2021]]は、precisionのmeta-controlを通じて注意状態への反省的介入をモデル化する。
- [[albarracinSharedProtentionsMultiAgent2024]]は、protentionをmulti-agent coordinationへ拡張する。
- [[wilsonActiveInferenceMethod2026]]は、active-inference構造を実装されたAIのagency phenotypeとして検査する方法を提供する。
- [[parvizi-wayneBodilyMindedSkill2026]]は、身体化されたskillが責任帰属に関係する規範的bridgeを示す。

それでも、計算的に実現された時間統合、meta-awareness、協調、身体的skillからmoral responsibilityは直ちに導けない。必要なのは、[[Functional Passive Synthesis]]から[[Reflective Self-Formation]]、[[Agentive Action Initiation]]、[[Intersubjective Agency]]へ至る複数条件の統合と、各条件がnormative ownershipを生む理由の独立した論証である。→ [[Computational Phenomenology Does Not Establish Moral Responsibility]]
