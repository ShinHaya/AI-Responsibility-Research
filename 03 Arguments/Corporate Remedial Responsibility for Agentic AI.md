---
type: argument
status: developing
created: 2026-08-23
tags:
  - ai-responsibility
  - corporate-responsibility
  - remediation
---

# Corporate Remedial Responsibility for Agentic AI

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Agentic Causal Provenance]]。
> **本研究で導入した作業概念**：[[Policy-Attested Agent Authorization]]。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Claim

platform上で外部AIエージェントが損害を生じさせた場合、provenanceはAIや利用者へ責任を転嫁するためではなく、企業が被害救済、原因究明、再発防止を遂行するための基盤として設計されるべきである。

Multiagent systemのdynamic traceabilityとdistributed ethical loggingには、[[nandyResponsibilityGapsAutonomous2026]]という先行例がある。

[[rongTrustExperienceGlitches2026]]は、delegation ambiguityとrevocation failureをtrust relationの破綻として分析する。

本Argumentの追加点は、provenanceをagentやuserへ責任転嫁するためではなく、platformが原因確定前から救済し、後に負担を再配分するための基盤として位置づける点にある。

## Argument

1. BYOAIでは、model provider、user、agent、platformのすべてが行為系列へ寄与しうる。
2. 「ユーザーが選んだAIだからユーザー責任」と一律に扱うと、不正の意図も予見可能性もない利用者へ損害を集中させる。
3. platformはAPI、権限、取引環境、禁止規則を設計し、危険なactionを拒否できる位置にある。
4. ゆえにplatformには、委任範囲と因果系列を保存し、取引停止、返金、相手方救済、policy改訂を実施できる体制を整える役割責任がある。

## Distinction

企業が救済責任を負うことは、すべての事故について企業だけが法的または道徳的に有責であることを意味しない。

これは原因が未確定な段階でも被害を放置せず、原因確定後には関係主体へ責任を適切に配分できる運用上の責任である。

## Trust Relation

agent事故はmodelの誤出力だけでなく、platformが表示した権限、承認、取消可能性と実際の行動がずれたときに生じる信頼関係の破綻でもある。

したがってincident reviewは、どのcomponentが故障したかに加えて、ユーザーが何を委任したと合理的に理解できたかを検証する必要がある。

## Related

- [[Agentic Causal Provenance]]
- [[Policy-Attested Agent Authorization]]
- [[Distributed Responsibility for AI Systems]]
- [[nandyResponsibilityGapsAutonomous2026]]
- [[rongTrustExperienceGlitches2026]]
