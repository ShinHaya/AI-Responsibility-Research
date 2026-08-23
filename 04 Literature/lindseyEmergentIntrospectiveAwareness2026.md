---
type: literature
status: unread
citekey: "lindseyEmergentIntrospectiveAwareness2026"
title: "Emergent Introspective Awareness in Large Language Models"
authors: "Jack Lindsey"
year: "2026"
doi: "10.48550/arXiv.2601.01828"
zotero: "zotero://select/library/items/SUDJGUTV"
tags:
  - literature
---

# Emergent Introspective Awareness in Large Language Models

## Bibliographic Information

**Citation Key:** @lindseyEmergentIntrospectiveAwareness2026

**Authors:** Jack Lindsey

**Year:** 2026


**DOI:** 10.48550/arXiv.2601.01828



**URL:** http://arxiv.org/abs/2601.01828



**PDF:** [Preprint PDF](zotero://select/library/items/MD8C5RKQ)



**Citation:** Lindsey, Jack. 「Emergent Introspective Awareness in Large Language Models」. arXiv:2601.01828. 査読前原稿, arXiv, 2026年1月5日. [https://doi.org/10.48550/arXiv.2601.01828](https://doi.org/10.48550/arXiv.2601.01828).


---

## Abstract

We investigate whether large language models can introspect on their internal states. It is difficult to answer this question through conversation alone, as genuine introspection cannot be distinguished from confabulations. Here, we address this challenge by injecting representations of known concepts into a model's activations, and measuring the influence of these manipulations on the model's self-reported states. We find that models can, in certain scenarios, notice the presence of injected concepts and accurately identify them. Models demonstrate some ability to recall prior internal representations and distinguish them from raw text inputs. Strikingly, we find that some models can use their ability to recall prior intentions in order to distinguish their own outputs from artificial prefills. In all these experiments, Claude Opus 4 and 4.1, the most capable models we tested, generally demonstrate the greatest introspective awareness; however, trends across models are complex and sensitive to post-training strategies. Finally, we explore whether models can explicitly control their internal representations, finding that models can modulate their activations when instructed or incentivized to "think about" a concept. Overall, our results indicate that current language models possess some functional introspective awareness of their own internal states. We stress that in today's models, this capacity is highly unreliable and context-dependent; however, it may continue to develop with further improvements to model capabilities.

---

## Core Idea

本研究は、現在のLLMが自らの内部状態について、限定的ながら機能的な
introspective awareness（内省的認識）を持つかを実験的に検証する。

通常の対話においてLLMが「私は〜を考えている」と自己報告しても、
それが実際の内部状態へのアクセスなのか、学習された言語パターンに基づく
confabulationなのかを区別することは難しい。

そこで本研究では、既知のconcept representationをモデル内部のactivationへ
人工的に注入し、モデルがその内部変化を検出・同定できるかを調べる。

その結果、現在のLLMには不安定かつcontext-dependentではあるものの、
自らの内部状態を検出・報告し、場合によってはその内部状態を一定程度
制御するfunctional introspective awarenessが存在する可能性が示された。


## Key Claims

- モデルは、内部activationへ人工的に注入されたconceptを一定の条件下で検出し、その内容を同定できる。

- モデルは、過去に存在したinternal representationを一定程度recallできる。

- モデルは、自らのinternal representationと外部から与えられたraw text inputを区別できる場合がある。

- モデルはprior intentionについての情報を利用し、自分自身が生成したoutputと人工的に挿入されたprefillを区別できる場合がある。

- モデルは、特定のconceptについて「考える」よう指示またはincentivizeされることで、そのconceptに対応するinternal activationを一定程度modulateできる。

- introspective awarenessの程度にはモデル間の差があり、本研究ではClaude Opus 4および4.1が比較的強い能力を示した。

- ただし、これらの能力は現在のLLMでは非常に不安定であり、contextやpost-training strategyにも依存する。

- したがって本研究は、人間と同等の内省能力や自己意識の存在を示すものではなく、限定的なfunctional introspectionの存在を示すものとして解釈すべきである。


## Relevance to My Theory

この研究は、私がAIの責任主体性の条件として考えている
[[Reflective Self-Formation]]の前提となる能力に直接関係する。

私の立場では、AIが責任主体となるためには、単にfirst-orderの選好や
行動傾向を持つだけでは不十分である。

Frankfurtのsecond-order desire / second-order volitionをAIへ拡張して考えるならば、
AIは少なくとも、

1. 自らの内部状態や選好傾向を対象化する
2. それを二階のレベルから評価する
3. 評価に基づいて自らの選好・判断傾向を変更する
4. その変更を将来の判断と行為へ持続的に反映する

という能力を必要とする。

Lindseyの研究が実験的証拠を与えているのは、主としてこのうち第1段階である。

したがって、

internal-state access
→ reflective evaluation
→ reflective self-modification
→ diachronic integration

という段階を区別する必要がある。

特に重要なのは、現在のLLMが内部状態を検出できることと、
その状態を「自分がどのような主体でありたいか」という規範的観点から
評価できることは別問題だという点である。

さらに、一時的なcontext内で内部状態を変更できることと、
その変更が経験として沈殿し、その後の選好・goal formation・行為へ
継続的に影響する[[Genetic and Diachronic Agency]]を持つことも区別しなければならない。


## My Evaluation

### Agree

本研究は、「現在のLLMには内省能力が存在しない」と一括して扱うことに対して、
重要な反例を提供していると考える。

特に重要なのは、LLMの言語的自己報告をそのまま内省の証拠として扱うのではなく、
activationへの介入を利用して、モデルの自己報告と内部状態の間に
因果的な関係が存在するかを検証している点である。

これはAIの自由意志や責任主体性を考える際にも重要である。

AIが自らの内部状態へ原理的にアクセスできないのであれば、
Frankfurt型の二階的自己評価や[[Reflective Self-Formation]]を実装することは
極めて困難だからである。

本研究は少なくとも、その最初の技術的障壁が原理的に不可能ではないことを示唆する。


### Disagree / Problems

本研究で示されたfunctional introspectionから、
自由意志・人格・道徳的責任を直接導くことはできない。

以下の能力は明確に区別する必要がある。

Introspective access
≠ Reflective evaluation
≠ Second-order volition
≠ Reflective self-formation
≠ Diachronic agency
≠ Moral responsibility

特に、モデルが自分の内部activationを検出できることは、
そのactivationを「望ましい／望ましくない」と規範的に評価することを意味しない。

また、activationを一時的にmodulateできることも、
自己の人格や選好構造を長期的に自己形成する能力とは異なる。

さらに本研究の能力はcontext-dependentであり、
現在のLLMに持続的な自己が存在することを示す証拠にはならない。


### Extension

私の理論から見た次の研究課題は、
introspectionそのものではなく「introspectionを利用した自己形成」である。

AIが、

internal state
→ introspection
→ normative evaluation
→ self-modification
→ memory / sedimentation
→ changed future salience and preferences
→ goal formation
→ action

という循環を形成できるかを検討する必要がある。

ここでHusserlの発生的現象学との接続が重要になる。

自己変容が単なる一時的なparameter adjustmentではなく、
過去の経験が沈殿し、現在の世界の見え方・実践的顕著性・予期・価値判断を
変化させる過程として実装されるならば、
[[Reflective Self-Formation]]は[[Genetic and Diachronic Agency]]へ接続される。

さらに、その自己形成史が特定のAI個体に帰属するためには
[[AI Individuation]]の問題を解決する必要がある。

AIの経験・memory・自己変容履歴が別のAIへ完全にコピー可能である場合、
「誰がその経験をしたのか」と
「誰がその経験によって自己形成されたのか」は同じ問題ではない。

したがって、将来的にはfunctional introspectionの研究を、
AIの自己形成・通時的主体性・個体性・責任帰属の問題へ拡張する必要がある。


## Related Concepts

- [[Reflective Self-Formation]]
- [[Genetic and Diachronic Agency]]
- [[AI Individuation]]
- [[Passive Synthesis]]
- [[Second-Order Volition]]
- [[Sourcehood]]


## Related Arguments

- [[Alternative Possibilities and Reflective Self-Formation]]
- [[Memory Possession Is Not Experience Authorship]]
- [[Can AI Possess Genetic and Diachronic Agency]]
- [[Can Distributed AI Be One Responsible Agent]]


## Questions Raised

- Functional introspectionはFrankfurt的なsecond-order volitionの必要条件と言えるか？

- Internal stateを「認識する」能力から、その状態を規範的に「評価する」能力へ移行するためには何が必要か？

- LLMは、自らの選好や判断傾向を対象化し、「この傾向を持ち続けたい／変更したい」と二階のレベルで評価できるか？

- introspectionに基づくself-modificationを、一時的なcontext内の変化ではなくpersistentな自己変容として実装できるか？

- 過去の自己変容がmemoryとして保存されるだけではなく、将来のsalience、valuation、goal formationを変化させる場合、それをHusserl的なsedimentationやhabitualityとして理解できるか？

- そのような自己形成の履歴が蓄積された場合、それをAI自身の「経験史」と呼ぶためには何が必要か？

- AIがあるmemoryを持っていることと、そのAI自身がその経験の発生的起源であることをどのように区別するべきか？

- AIの経験史・memory・自己変容履歴を別のAIへ完全にコピーした場合、コピー先のAIは同じ自己形成史を持つと言えるのか？

- 同一の自己形成史を持つ複数のAIが存在できるならば、道徳的責任を帰属させるための[[AI Individuation]]は何によって成立するのか？

- Functional introspection、reflective self-formation、genetic/diachronic agencyがすべて実装されたとしても、それだけでAIを道徳的責任主体と認められるのか？