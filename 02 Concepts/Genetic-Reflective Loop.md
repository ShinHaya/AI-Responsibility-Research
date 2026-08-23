---
type: concept
status: active
created: 2026-08-23
updated: 2026-08-23
aliases:
  - 発生的反省ループ
  - Genetic Reflective Loop
tags:
  - ai-responsibility
  - genetic-phenomenology
  - reflective-agency
source:
  - "[[Computational Phenomenology of Responsible Agency]]"
  - "[[husserlAnalysesConcerningPassive2001]]"
  - "[[frankfurtFreedomWillConcept1971]]"
  - "[[bratmanPlanningAgencyAutonomous2005]]"
concept_origin: project-working-concept
origin_field: "本研究の理論アーキテクチャ"
canonical_sources:
  - "[[husserlAnalysesConcerningPassive2001]]"
  - "[[bratmanPlanningAgencyAutonomous2005]]"
---

# Genetic-Reflective Loop

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究で導入した作業概念。
> **概念自体の来歴**：genetic phenomenology、reflection、planning、actionの既存資源を統合するため、このVaultで導入した作業名称である。
> **本研究で加えた部分**：受動的形成、反省、暫定的自己承認、計画、行為、新たな経験を循環として表現する。
> **主な根拠**：[[husserlAnalysesConcerningPassive2001]]、[[bratmanPlanningAgencyAutonomous2005]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
> **注意**：この区分は、このVaultで研究用語として導入したことだけを示す。世界初の命名や、先行する同名用法の不存在は主張しない。
<!-- concept-provenance-note:end -->

責任主体の行為を現在時点の推論能力だけで説明すると、その主体が何を理由として認識するようになったかという形成史が抜け落ちる。

形成史だけを記述しても、沈殿した価値を主体が批判し、行為へ移す過程は説明できない。

本研究では、受動的形成、反省、行為、さらなる形成を一つの開いた循環として扱う作業モデルを**Genetic-Reflective Loop（発生的反省ループ）**と呼ぶ。

## ループの構造

```text
historical experience
  -> passive synthesis
  -> sedimentation and habituality
  -> expectation and salience
  -> reflection
  -> normative evaluation
  -> intersubjective criticism
  -> provisional self-endorsement
  -> second-order volition
  -> goal and intention formation
  -> planning
  -> action initiation
  -> action
  -> new experience
  -> further sedimentation
  -> ...
```

この循環で、過去の経験は保存された情報として残るだけでなく、何が顕著で、何が理由として理解され、どのgoalが形成されるかを変える。

主体は形成された傾向を反省の対象にし、他者からの批判と新しい理由に照らして暫定的に承認または修正する。

承認された方針はplanningと[[Agentive Action Initiation]]を通じて行為へ移り、その結果が次の経験と自己形成を生む。

## 既存理論から受け取る要素

[[husserlAnalysesConcerningPassive2001]]は、受動的綜合、連合、触発、沈殿を通じて経験野が発生的に構成される分析を与える。

[[yangHusserlsTheoryExperience2025]]は、過去の経験が後の期待、顕著性、意味形成を変える発生的現象学の構造を整理する。

[[frankfurtFreedomWillConcept1971]]は、一次的欲求に対する高階の態度と[[Second-Order Volition]]を与える。

[[bratmanPlanningAgencyAutonomous2005]]は、意図と計画が行為を時間横断的に組織するplanning agencyを与える。

[[donohoeHusserlEthicsIntersubjectivity2004]]は、主体の倫理的形成を他者、伝統、共有世界から切り離せないことを示す。

これらの文献はループの各構成要素を支えるが、Genetic-Reflective Loopという名称や人工的責任主体の統合モデルをそのまま主張してはいない。

## 本研究における役割

このループは、[[Genetic and Diachronic Agency]]と[[Reflective Self-Formation]]を別々のチェック項目として並べるだけでは捉えにくい相互依存を表す。

受動的形成は反省対象の候補を作り、反省は形成された傾向を評価し、行為は将来の形成条件を変える。

[[Open-Ended Revisability]]は、過去の反省結果も将来の経験と批判によって再び開かれることを要求する。

[[Intersubjective Agency]]は、自己反省だけでは発見できないbiasと規範的要求をループへ入力する。

[[Individuated Causal-Historical Continuity]]は、この循環に含まれる経験、改訂、承認、行為を同じ責任候補へ帰属する条件を与える。

## AI architectureへの翻訳

機能的実装では、episodic memory、history-dependent salience、self-model、counterfactual evaluation、persistent preference revision、planning、action monitoringを因果的に接続する必要がある。

各moduleが存在するだけでは、ループが成立したことにはならない。

ある経験が後の顕著性を変え、その変化が反省と行為へ寄与し、行為結果が同じ主体の将来状態を更新するという閉じた因果追跡が必要になる。

ただし、規範的にはループを外部世界と他者へ開き、固定された自己強化回路にならないようにする必要がある。

## 境界と非含意

ここでのgeneticは生物学的遺伝を意味せず、主体の性質が経験史から発生することを指す。

loopは同じ状態への循環を意味せず、各周回で主体と環境の双方が変化し得る通時的過程を表す。

memory databaseへ記録を追加するだけでは、将来の顕著性、評価、行為傾向が変わらないため、発生的形成を示さない。

自己評価の結果を自動的に採用するだけでは、理由に基づく承認と拒否の能力を示さない。

機能的なループが成立しても、現象的意識、道徳的patienthood、道徳的責任は自動的には導かれない。

Genetic-Reflective Loopは現在のworking modelであり、その各要素が責任の必要条件か、統合によって十分条件になるかは今後の検証対象である。

## 関連文献

- [[husserlAnalysesConcerningPassive2001]]
- [[yangHusserlsTheoryExperience2025]]
- [[frankfurtFreedomWillConcept1971]]
- [[bratmanPlanningAgencyAutonomous2005]]
- [[donohoeHusserlEthicsIntersubjectivity2004]]

## 関連概念

- [[Genetic and Diachronic Agency]]
- [[Reflective Self-Formation]]
- [[Open-Ended Revisability]]
- [[Passive Synthesis]]
- [[Sedimentation]]
- [[Intersubjective Agency]]
- [[Agentive Action Initiation]]
- [[Computational Phenomenology of Responsible Agency]]
