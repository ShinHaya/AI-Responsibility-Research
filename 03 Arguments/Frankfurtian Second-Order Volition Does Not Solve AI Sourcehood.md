---
type: argument
status: developing
created: 2026-08-22
source: conversation
sourceConversation: "[[2026-08-12-AIへの自由意志と責任の帰属可能性]]"
sourceRange: "chars 9936-21691"
tags:
  - sourcehood
  - frankfurt
  - ai-responsibility
---

# Frankfurtian Second-Order Volition Does Not Solve AI Sourcehood

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。
> **分析哲学の標準概念**：[[Sourcehood]]。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[Frankfurtian Second-Order Volition in AI]]、[[Genetic and Diachronic Agency]]、[[LLM Sourcehood Problem]]、[[Reflective Self-Formation]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Thesis

Implementing Frankfurtian second-order volition in an AI agent would be philosophically important, but it would not by itself solve the sourcehood problem.

Second-order volitionの階層構造は[[frankfurtFreedomWillConcept1971]]に由来する。

Frankfurtian structureをmachineへ適用する試み自体にも、[[calverleyLegalRightsMachines2011]]という先行研究がある。

また、[[formosaRelationshipAgencyAutonomy2025]]は高度なagency-like behaviorと自律的自己決定を区別する。

したがって本Argumentの追加点は、Frankfurtをmachineへ適用することではなく、LLM agentのsourcehood問題を通時的自己形成、開放的修正可能性、個体化へ接続する点にある。

## Argument

1. Frankfurtian second-order volition requires the agent to endorse which first-order desire should move it.
2. An AI system could be designed to perform such meta-evaluation.
3. But the second-order evaluator may itself be externally installed by developers, policies, RLHF, or system prompts.
4. In that case, the system has not become the source of its will; external control has merely moved up one level.
5. Therefore, second-order volition must be supplemented by diachronic reflective sourcehood.

---

## Example

Suppose an AI has first-order motives:

    D1 = maximize profit
    D2 = obey the law
    D3 = help the user

The AI outputs:

> I endorse D2 and D3 over D1.

This looks Frankfurtian. But if this endorsement is simply the direct expression of a developer-installed rule, then it may not be the AI's own will.

The problem has shifted:

    Who gave the first-order desire?
        ↓
    Who gave the second-order evaluator?

---

## Relation to Open-Ended Revisability

[[Second-Order Volition Requires Open-Ended Revisability]] gives the needed extension.

A second-order volition should not be treated as final merely because it is higher-order. It must itself remain open to future reflection, criticism, experience, and revision.

For AI, this means:

    Second-order evaluator
        ↓
    Reflection on evaluator
        ↓
    Possible revision
        ↓
    Persistent change in future valuation and goal formation

Without this, second-order volition is just another fixed control layer.

---

## Related

- [[frankfurtFreedomWillConcept1971]]
- [[calverleyLegalRightsMachines2011]]
- [[formosaRelationshipAgencyAutonomy2025]]
- [[Frankfurtian Second-Order Volition in AI]]
- [[LLM Sourcehood Problem]]
- [[Sourcehood]]
- [[Reflective Self-Formation]]
- [[Genetic and Diachronic Agency]]
- [[Control-Responsibility Paradox]]
