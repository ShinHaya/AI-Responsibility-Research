---
type: index
status: active
created: 2026-08-23
updated: 2026-08-23
tags:
  - concept-provenance
  - methodology
---

# Concept Provenance Registry

<!-- concept-provenance-note:start -->
> [!info] このレジストリの役割
> 概念の由来と、このVaultでの再構成・追加を別々に記録する。
> 「標準」は用語や論点が定着していることを示し、その理論が真であるとの合意を意味しない。
<!-- concept-provenance-note:end -->

このレジストリは、概念自体の知的来歴と、この研究で行った再定義、統合、命名を区別する。

## 判定の単位

分類対象はConcept Noteの主見出しが指す概念である。

同じノートが標準概念の説明と本研究独自の下位区分を含む場合、`concept_origin`は主概念の来歴を表し、本文の「本研究で加えた部分」が差分を表す。

したがって、ノート全体を既存か独自かの二値へ押し込まない。

`sourceConversation`や既存の`source`は、会話や文献からノートを作成した経路を示すために使われてきたfieldである。

これらは`concept_origin`の代わりにならず、命名の優先権も証明しない。

## 四つの区分

### 分析哲学の標準概念

`concept_origin: established-analytic-free-will`

分析哲学の自由意志論または道徳的責任論で、用語または論点として定着している概念である。

ここでの「標準」は、その理論が真である、または研究者間で定義が完全に一致しているという意味ではない。

### 隣接分野・文献由来

`concept_origin: borrowed-adjacent-field`

現象学、行為論、認知科学、AI倫理、AI研究、法哲学、STSなどから借用した概念、または特定文献の主張に由来する概念である。

この区分は、分析哲学の自由意志論で一般的な概念ではないことを示すが、本研究が最初に作ったことも意味しない。

### 本研究による再構成

`concept_origin: project-extension`

既存概念や複数文献の資源を、AI responsibilityの問題へ適用、統合、限定または強化した概念である。

既存の基礎と本研究の追加をConcept Noteの来歴calloutで別々に記録する。

### 本研究で導入した作業概念

`concept_origin: project-working-concept`

このVaultで研究上の区別、仮説またはarchitectureを表すために導入した名称である。

この区分は、この研究内での導入を示すだけであり、世界初の命名、先行する同名用法の不存在、完成した理論であることを主張しない。

## 分析哲学の標準概念

| Concept Note | 標準的な核 | 本研究での扱い |
|---|---|---|
| [[Free Will]] | 自由な意志と行為の成立条件を問う中心概念 | 複合的な高階agency competenceという再構成案を標準概念から分離する |
| [[Alternative Possibilities]] | 別様に行為できたかを問う論点 | AI向けのmeans、goal、normの三層は本研究の追加である |
| [[Second-Order Volition]] | Frankfurtの二階の意志 | AI適用と開放的修正可能性は別の拡張として扱う |
| [[Reasons-Responsiveness]] | FischerとRavizza系の理由応答性 | AIではgoal、norm、形成史、個体化の追加条件を検討する |
| [[Sourcehood]] | 行為が主体自身に由来する条件 | diachronic reflective sourcehoodは本研究の再構成である |
| [[Responsibility]] | 因果的、役割上、道徳的、法的責任の区別 | AI責任と証拠基盤の関係を追加で整理する |

## 隣接分野・文献由来

| Concept Note | 主な由来 | 本研究での扱い |
|---|---|---|
| [[AI Global Workspace]] | AI解釈可能性研究とglobal workspaceの類比 | 反省的agencyへの含意を検討する |
| [[Artificial Moral Agency]] | AI倫理と情報倫理 | 機能的moral agencyと強い責任主体性を区別する |
| [[Computational Phenomenology]] | 計算論的神経科学と現象学 | responsible agencyの三水準方法へ拡張する |
| [[Functional Emotion in AI]] | LLM内部のemotion-like機構研究 | 通時的形成と責任への含意を検討する |
| [[Habituality]] | Husserl現象学 | AIのdispositionとの機能的対応を検討する |
| [[Moral Crumple Zone]] | ElishのAI倫理・STS研究 | 組織的責任と救済責任へ接続する |
| [[Passive Synthesis]] | Husserl現象学 | responsible agencyの形成史へ接続する |
| [[Responsibility Gap]] | Matthias以降のAI責任論 | 複数の責任類型へ分解して検討する |
| [[Sampling Is Not Choosing]] | Keshetの生成AI批判 | Martelaとの対比からagency levelを明確化する |
| [[Sedimentation]] | Husserl現象学 | AI memoryと通時的dispositionを区別する |
| [[Shared Protention]] | multi-agent active inference研究 | 共同予測と一個体のdistributed agencyを区別する |

## 本研究による再構成

| Concept Note | 既存の基礎 | 本研究の追加 |
|---|---|---|
| [[AI Individuation]] | AIの数え上げ、copy、branching、scaffolded system | 責任目的の統一的な個体境界テスト |
| [[Agency-Level Alternative Possibilities]] | Alternative PossibilitiesとMartelaの機能的自由 | token samplingからreason-owned alternativesまでの階層化 |
| [[Agentic Causal Provenance]] | agentic AIのprovenance、auditability、authenticated delegation | 上位責任判断の認識的前提と証拠水準の整理 |
| [[Agentive Action Initiation]] | 行為論、planning agency、goal generation | goal形成からanswerabilityまでを結ぶAI責任条件 |
| [[Distributed Artificial Agent]] | distributed cognition、shared agency、AI identity | 統合された自己形成と統制による責任主体境界 |
| [[Frankfurtian Second-Order Volition in AI]] | FrankfurtとCalverleyによるmachine適用 | LLM sourcehood、通時性、個体化との統合 |
| [[Functional Passive Synthesis]] | Husserlian passive synthesisとactive inference | AI向けの限定的な機能類比 |
| [[Genetic and Diachronic Agency]] | genetic phenomenologyとplanning agency | 形成史、反省、未来行為の統合条件 |
| [[Intersubjective Agency]] | 現象学、relational autonomy、shared agency | AI責任のための批判・理由交換・規範修正条件 |
| [[LLM Sourcehood Problem]] | 標準的sourcehoodとAI autonomy論 | LLM、prompt、scaffold、設計依存の統合問題 |
| [[Normative Contestability]] | Pettitのnon-dominationとcontestability | action、goal、normの三水準での異議申立て |
| [[Open-Ended Revisability]] | Frankfurt批判、self-variation、ethical renewal | 高階の自己承認を通時的に開き直す条件 |
| [[Practical Alternative Possibilities]] | Alternative Possibilities、reasons-responsiveness、robust alternatives | means、goal、normの三層から成る実践的能力 |
| [[Precision-Weighted Affection]] | Husserlian Affektionとprecision weighting | 両者の限定的な機能対応仮説 |
| [[Reflective Self-Formation]] | 意志階層説、reflective endorsement、現象学的自己形成 | AI責任のための通時的・規範的統合条件 |

## 本研究で導入した作業概念

| Concept Note | 研究上の役割 | 優先権に関する限定 |
|---|---|---|
| [[Genetic-Reflective Loop]] | 受動的形成、反省、計画、行為を循環として結ぶarchitecture | このVault内の統合モデルであり、世界初の名称とは主張しない |
| [[Individuated Causal-Historical Continuity]] | 情報内容と個体化された経験・行為史を区別する | このVault内の責任帰属基準であり、同名用法を網羅確認したとは主張しない |
| [[Internalized Normative Self-Control]] | 外部guardrailと形成された自己統制を区別する | 既存のself-controlとnorm internalizationを組み合わせた作業名称である |
| [[Personal Asset Data Store]] | Personal Data Storeを所有物データへ拡張する | この研究の構想名であり、文字列の世界初使用とは主張しない |
| [[Policy-Attested Agent Authorization]] | 委任、identity、policy enforcementを検証可能な証明へ結ぶ | このVaultの作業名称であり、近接する技術や同名用法の不存在は主張しない |

## Literature Noteの出自表示

Literature Noteでは、frontmatter、`Bibliographic Information`、`Abstract`を保護する。

それ以外のH2には次の出自表示を置く。

- **文献由来**：当該文献の内容を要約する欄であり、翻訳と要約の表現はノート作成者による。
- **本研究による分析**：比較、評価、AI責任論への応用または理論的拡張である。
- **本研究による整理**：関連リンク、問いまたは作業メモであり、文献著者の主張そのものではない。
- **混合・要確認**：文献要約と本研究の分析を安全に分離できないため、個別文の帰属確認が必要である。

「文献由来」は、分析哲学で一般に認められた標準概念であることを意味しない。

著者固有の提案、論争的な立場、隣接分野のtechnical termも含む。

## Canonical link方針

同じ概念に複数のworking nameがある場合、新しい空ノートを増やさず、標準定義または現在のConcept Noteへalias linkを張る。

| 旧表記・下位概念 | Canonical link |
|---|---|
| Genetic-Diachronic Identity | [[Individuated Causal-Historical Continuity]] |
| Higher-Order Volition | [[Second-Order Volition]] |
| Guidance Control | [[Reasons-Responsiveness#Guidance Control]] |
| Mechanism Ownership | [[Reasons-Responsiveness#Mechanism Ownership]] |
| Provisional Self-Endorsement | [[Open-Ended Revisability#Provisional Self-Endorsement]] |
| Counterfactual Self-Variation | [[Open-Ended Revisability#Counterfactual Self-Variation]] |
| Moral、Legal、Role、Causal Responsibility | [[Responsibility]]の各節 |

## 更新規則

新しいConcept Noteを追加するときは、`concept_origin`を四値のいずれかに固定する。

`origin_field`には主な学問領域を記録する。

`canonical_sources`には判定を支える主要文献だけを置き、網羅的bibliographyとはみなさない。

分類を変更するときは、Concept Noteのcalloutとこのレジストリを同時に更新する。

同じ名称の既存用法を後から発見した場合、本研究の理論的差分が残っていても、`project-working-concept`から`project-extension`または`borrowed-adjacent-field`へ変更する。
