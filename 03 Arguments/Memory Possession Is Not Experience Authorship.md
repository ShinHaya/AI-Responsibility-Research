---
type: argument
status: developing
created: 2026-08-12
---

# Memory Possession Is Not Experience Authorship

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：該当なし。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Thesis

AIが他のAIのepisodic memoryを完全にコピーしても、その経験の発生的起源までコピーされたとは限らない。

Memory possession ≠ Experience authorship.

Autobiographical narrativeとnumerical identityの区別には[[reaMetaphysicsNarrativeSelf2022]]が、外部resourceへ分散したmemoryには[[heersminkNarrativeSelfDistributed2018]]が先行する。

Branching後のidentityとresponsibilityの分離は[[walkerBranchingNotBug2020]]で論じられ、AI memory governanceには[[cuadrosGovernedCollaborativeMemory2026]]という先行研究がある。

本Argumentの追加点は、AI memoryについてoriginとappropriationを二層化し、experienced-by、copied-from、endorsed-byなどのrelationとして追跡する点にある。

## Thought Experiment

AI-Aが出来事Eを経験する。

その後Eについての完全なmemoryをAI-Bへコピーする。

BはEについてAと同一の内部表象を持つかもしれない。

しかし、

A experienced E

と

B possesses a memory representation originating from A's experience of E

は区別できる。

## Implication

AI memoryにはcontentだけでなくprovenanceが必要である。

- experienced-by
- copied-from
- learned-from
- reflected-upon-by

などを区別する必要がある。

## Open Problem

コピー後にBがそのmemoryを自己物語へ完全に統合した場合でも、この区別を維持すべきか？

→ [[Can Distributed AI Be One Responsible Agent]]

## Provenance Is Relational, Not Merely Metadata

UUIDはthin traceabilityを与えるが、experience authorshipの全てではない。最低限、episodeに次のrelationを区別する必要がある。

```text
experienced-by
observed-from
copied-from
learned-from
endorsed-by
revised-by
acted-upon-by
```

責任帰属で重要なのは、motivationのoriginだけでなく、受領した主体がそれをどう評価し、endorseまたはrejectし、actionへ接続したかである。A由来のgoalをBが受け取っても、`copy -> reflection_B -> endorsement_B -> initiation_B`があればB固有の責任関連的因果系列が生じる。

## Narrative Integration

[[ahmedNarrativeSelfInstantiated2026]]はmemory architectureによりpersistent functional identityを構成できる可能性を示すが、prompt dependenceとself-report中心の評価には注意が必要である。コピーされたmemoryを自己物語へ統合することはidentity dispositionを形成しうるが、過去のevent authorshipを遡及的に変更しない。

したがって、narrative ownershipとcausal originを二層で保持する。

- **origin**: その出来事・状態変化がどのprocessで発生したか。
- **appropriation**: 後の主体がそれを自分の理由・自己物語へどう統合したか。

## Related Literature

- [[reaMetaphysicsNarrativeSelf2022]]
- [[heersminkNarrativeSelfDistributed2018]]
- [[walkerBranchingNotBug2020]]
- [[cuadrosGovernedCollaborativeMemory2026]]
- [[ahmedNarrativeSelfInstantiated2026]]
