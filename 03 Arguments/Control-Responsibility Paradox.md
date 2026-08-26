---
type: argument
status: developing
created: 2026-08-12
---

# Control-Responsibility Paradox

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Normative Contestability]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Initial Formulation

責任とcontrolの関係自体には、[[fischerResponsibilityControlTheory1998]]のguidance controlや、[[pettitRepublicanismTheoryFreedom1999]]のnon-dominationという先行議論がある。

また、人間へ責任が集中する構造は、[[elishMoralCrumpleZones2019]]がmoral crumple zoneとして分析する。

本Argumentが導入するのは、企業がAIを信頼するための一方的controlを強めるほどAI自身への責任帰属を弱めるという特定の緊張を、Control-Responsibility Paradoxとして定式化する点である。

企業がAIを信頼して重要な仕事を任せるためには、AIを強くcontrolしたくなる。

しかしcontrolを強くするほどAI自身のAlternative PossibilitiesやReflective Self-Formationが失われ、責任をAI自身に帰属できなくなる。

したがって、

「責任を負わせられるほど信頼できるAIにするほど、AIに責任を負わせられなくなる」

というparadoxが生じる。

## Revision

このparadoxは「信頼」と「他行為可能性」を混同すると生じる。

仕事を信頼して任せられる条件として重要なのは、悪い行為をする可能性ではなく、タスクを完遂するCompetenceである。

責任主体に必要なAlternative Possibilitiesは、

- タスク遂行方法についての選択
- 不正なタスクへの異議申し立て

として存在すればよい。

## Remaining Problem

社会的正義を自己形成によって内在化した結果として不正をしないことと、外部guardrailによって不正が技術的に不可能であることは区別しなければならない。

## Resolution by Two Kinds of Reliability

パラドックスは`reliability`を二つに分けることで部分的に解消される。

```text
externally guaranteed reliability
  = permissions, hard constraints, output blocks
  -> autonomy and attributable control may decrease

internally constituted reliability
  = experience, competence, reflection, habitualized norms
  -> autonomy and responsibility capacity may increase
```

したがって「信頼できるほど責任を負わせられない」のではない。**制御者が一本道を保証することでのみ信頼できるAI**ほど、その行為をAI自身へ帰属しにくい。他方、正しい理由を経験から内在化し、必要時に規範を問い直せるAIは、信頼性と責任能力を同時に高めうる。

## Residual Paradox

完全な解消にはならない。企業がAI自身へ責任を移したいなら、AIへ[[Normative Contestability]]と実効的な異議申立て経路を与える必要があるが、それは企業の最終的controlを弱める。したがって残る対立は、reliabilityとresponsibilityではなく、**一方的支配と責任主体の自立**の間にある。

AIを「新人」から昇格させる基準は規則への完全服従ではなく、(1) task competence、(2)理由に基づく安定した自己統制、(3)上位規範の批判可能性、(4)監査可能な自己形成史である。

## Related Literature

- [[fischerResponsibilityControlTheory1998]]
- [[pettitRepublicanismTheoryFreedom1999]]
- [[elishMoralCrumpleZones2019]]
