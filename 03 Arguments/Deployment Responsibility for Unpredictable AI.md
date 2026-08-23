---
type: argument
status: seed
created: 2026-08-22
source: conversation
sourceConversation: "[[2026-08-12-AIへの自由意志と責任の帰属可能性]]"
sourceRange: "chars 0-9936"
tags:
  - ai-responsibility
  - deployment
---

# Deployment Responsibility for Unpredictable AI

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：[[Responsibility Gap]]。
> **本研究による再構成**：該当なし。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Thesis

Even if a deployer cannot predict the exact output or action of an AI system, the deployer may still bear responsibility for choosing to place an unpredictable system into a particular operational environment.

この主張は、学習systemの予測不能性からresponsibility gapを論じた[[matthiasResponsibilityGap2004]]への応答として位置づく。

[[coeckelberghResponsibilityAttribution2020]]は多主体と時間的controlの複雑さを扱い、[[tigardNoTechnoResponsibilityGap2021]]はtechnologyによる不可避の責任空白を否定する。

本Argumentの追加点は、これらの議論を個別出力ではなくdeployment decisionを責任対象とする形で整理する点にある。

## Argument

1. Some AI systems are not fully predictable at the level of concrete actions.
2. Unpredictability does not by itself imply that no one is responsible.
3. A human or organization may be responsible for the decision to deploy a system with known classes of risk.
4. Therefore, responsibility can sometimes be assigned to the deployment decision rather than to the specific downstream action.

## Relevance

This argument is a response to a strong reading of [[Responsibility Gap]]. It shifts the object of responsibility from direct control over the harmful act to responsible governance of risky deployment.

## Related

- [[matthiasResponsibilityGap2004]]
- [[coeckelberghResponsibilityAttribution2020]]
- [[tigardNoTechnoResponsibilityGap2021]]
- [[Organizational Responsibility for AI Deployment]]
- [[Distributed Responsibility for AI Systems]]
- [[Control-Responsibility Paradox]]
