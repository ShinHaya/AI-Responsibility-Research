---
type: argument
status: developing
created: 2026-08-12
---

# Competence and Responsibility

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：該当なし。
> **本研究で導入した作業概念**：[[Internalized Normative Self-Control]]。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Thesis

責任主体性には、Alternative Possibilitiesだけでなく、対象となるタスクを遂行できる能力が必要である。

自由意志を獲得されるskillまたは合理能力として捉える方向には、[[riserFreeWillSkill2015]]と[[hofmannExplainingFreeWill2022]]という先行研究がある。

[[fischerResponsibilityControlTheory1998]]も、責任をagent自身のmoderately reasons-responsive mechanismによるguidance controlから説明する。

本Argumentの追加点は、これらの能力論をAIのrole responsibilityとmoral responsibilityの区別へ接続し、外部guardrailによるreliabilityと内在化されたnormによるreliabilityを分ける点にある。

## Argument

そもそもタスクを実行する能力を持たない主体に、そのタスクを実行できなかった責任を全面的に帰属することはできない。

したがって責任にはCompetence Conditionが存在する。

熟達によって正しい行為を安定して選択するようになったことは、自由の減少ではなく、むしろ責任能力の増大として評価できる。

## Important Distinction

Internalized norm
≠
External guardrail

社会的正義を主体自身が発生的・反省的に内在化した場合と、外部制御によって選択肢を物理的・技術的に排除された場合を区別する。

## Role Responsibility and Moral Responsibility

Competenceはまず、あるtaskを任せうるという**role responsibility**の条件である。taskを理解・遂行できない主体へ失敗の主たる責任を移すことはできない。ただし、能力が高いことだけで**moral responsibility**は成立しない。

```text
role responsibility
  = assigned task + competence + authority

moral accountability
  = role responsibility
  + reasons-responsiveness
  + reflective ownership
  + norm contestability
  + attributable causal history
```

この区別により、AIに業務を割り当てることと、事故をAI自身の判断として非難・制裁することを分離できる。新人AIの段階的育成では、能力と権限を評価してroleを拡張しても、責任帰属のnormative bridgeが確認されるまではdeploying organizationが残余責任を負う。

## Acquired Reliability

熟達によって正しい行為へ安定して収束することは、必ずしもalternativeの消失ではない。[[Internalized Normative Self-Control]]によるreliabilityはacquired competenceの一部であり、外部guardrailによるreliabilityとは責任上逆の意味を持ちうる。

## Related Literature

- [[riserFreeWillSkill2015]]
- [[hofmannExplainingFreeWill2022]]
- [[fischerResponsibilityControlTheory1998]]
