---
type: argument
status: developing
created: 2026-08-23
tags:
  - ai-responsibility
  - accountability
  - provenance
---

# Attributable Causation Is an Epistemic Precondition for Higher Responsibility

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：[[Responsibility]]。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Agentic Causal Provenance]]、[[AI Individuation]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Claim

AIの役割責任、説明義務、法的責任、道徳的責任を判断するには、結果を生じさせた行為主体と因果系列を同定できなければならない。

したがって、**帰属可能な因果関係**は上位の責任形態の認識的必要条件である。

Agent lifecycle全体のexplicit provenanceを責任インフラとする考えには、[[huResponsibleAgenticAI2026]]という直接の先行研究がある。

[[nianAuditableAgents2026]]はauditabilityをaccountabilityの認識的前提として区別し、[[southAuthenticatedDelegationAuthorized2025]]と[[otsukaAIIdentityStandards2026]]は委任とoperational identityの記録要件を示す。

本Argumentの追加点は、これらをResponsibility Stackへ整理し、attributable causationを上位責任の十分条件ではなく帰属判断の認識的前提として限定する点にある。

## Argument

1. 役割責任の評価には、どのagentにどの役割と権限が割り当てられていたかを特定する必要がある。
2. answerabilityの評価には、当該agentが実際に参照した情報、適用されたpolicy、実行したactionを再構成する必要がある。
3. 法的責任や道徳的責任の評価にも、問題の結果と候補主体の行為との関係が必要になる。
4. agent identityと因果系列を追跡できなければ、これらの評価対象を確定できない。
5. ゆえにidentificationとcausal traceabilityは、上位責任の成立条件ではなく、その帰属判断を可能にする認識的前提である。

## Responsibility Stack

```text
Agent Identification
  → Causal Traceability
  → Role Responsibility
  → Answerability and Accountability
  → Legal or Moral Responsibility
```

この順序は、下位層だけで上位層が成立するという十分条件を示さない。

たとえば完全な監査ログがあっても、AIが道徳的非難に値するとは限らない。

## Post-Hoc Explanation Objection

行為後にLLMへ理由を質問して得た文章は、因果的説明の証拠にならない。

生成された理由は事後合理化である可能性があるため、行為時点のprovenanceと照合する必要がある。

AIに課しうる説明義務は、自由意志や意識を前提とする道徳的責任ではなく、役割に由来する機能的answerabilityとして位置づけられる。

ただし「AI自身の説明責任」という表現は、説明生成主体と責任主体を混同させる。

より正確には、AIは業務経過を報告する役割上の義務を担い、人間または組織がその報告をprovenanceと照合して責任判断を行う。

## Distributed Causation Objection

一つの結果には、user instruction、agent、local skill、外部のprompt injection、過剰な権限、platform guardrailの不備が共同で寄与しうる。

したがって帰属可能な因果関係は「どのAIのせいか」を一つ選ぶ手続きではなく、寄与関係をprovenance graphとして分解する手続きである。

## Related

- [[Agentic Causal Provenance]]
- [[Distributed Responsibility for AI Systems]]
- [[Responsibility#Role Responsibility|Role Responsibility]]
- [[AI Individuation]]
- [[nianAuditableAgents2026]]
- [[huResponsibleAgenticAI2026]]
- [[southAuthenticatedDelegationAuthorized2025]]
- [[otsukaAIIdentityStandards2026]]
