---
type: concept
status: developing
created: 2026-08-22
source: conversation
sourceConversation: "[[2026-08-12-AIへの自由意志と責任の帰属可能性]]"
sourceRange: "chars 9936-21691"
tags:
  - free-will
  - ai-responsibility
  - alternative-possibilities
concept_origin: project-extension
origin_field: "分析哲学の自由意志論・AI agency研究"
canonical_sources:
  - "[[martelaArtificialIntelligenceFree2025]]"
  - "[[keshetSamplingNotChoosing2026]]"
---

# Agency-Level Alternative Possibilities

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究による再構成。
> **概念自体の来歴**：Alternative Possibilitiesという標準論点と、MartelaによるLLM agent水準の機能的自由の議論を基礎とする。
> **本研究で加えた部分**：token samplingを、goal、reason、plan、affordanceの水準で表象・評価・選択される代替から区別する。
> **主な根拠**：[[martelaArtificialIntelligenceFree2025]]、[[keshetSamplingNotChoosing2026]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Core Idea

Agency-level alternative possibilities are practical alternatives described at the level of an agent's reasons, goals, plans, and action options, rather than at the lower level of token sampling, deterministic computation, or physical microstates.

[[martelaArtificialIntelligenceFree2025]] is important because it argues that generative LLM agents can have functional free will partly because they can recognize and choose among multiple possible courses of action at the agent level.

---

## The Level Distinction

The key move is to distinguish:

    Computational / physical level
        tokens, weights, sampling, state transitions

from:

    Agency level
        goals, plans, reasons, environmental affordances, possible actions

On a compatibilist reading, a system may be deterministic or probabilistic at the lower level while still having meaningful alternatives at the higher agent level.

For example, a Minecraft LLM agent might deliberate among:

- build shelter
- search for food
- craft tools
- avoid danger
- explore new terrain

The question is whether these are merely descriptions imposed by observers, or whether they function as action possibilities for the agent itself.

---

## Difference from Sampling

Agency-level alternatives are not identical with multiple possible sampled outputs.

    Output distribution
        ≠
    Practical space of alternatives

A token sampler can generate different continuations without possessing practical alternatives in the morally relevant sense. For responsibility, the alternatives must be connected to reasons, commitments, self-attribution, and action guidance.

This is the central pressure from [[keshetSamplingNotChoosing2026]].

---

## Relevance to My Theory

This concept refines [[Alternative Possibilities]] for AI.

The relevant question is not:

> Could the model have generated a different token?

but:

> Did the AI agent encounter multiple action paths as practical possibilities and select among them through an integrated agency process?

This provides the first part of the model:

    Free
        =
    Agency-Level Alternative Possibilities

But it is not sufficient for responsibility. It must be connected to:

    Will
        =
    Frankfurtian Second-Order Volition
        +
    Sourcehood

---

## Open Questions

- Are LLM agent plans genuine practical possibilities or merely post hoc descriptions of sampled text?
- Can a system have agency-level alternatives without phenomenal experience?
- Are practical alternatives observer-relative or system-internal?
- What architecture would make alternatives action-guiding rather than merely generated?
- How does agency-level AP relate to [[Practical Alternative Possibilities]]?

## Related

- [[Alternative Possibilities]]
- [[Sampling Is Not Choosing]]
- [[Free Will Conditions for Artificial Moral Responsibility]]
- [[martelaArtificialIntelligenceFree2025]]

## Genetic Constitution of Practical Alternatives

Practical alternatives are not merely options listed by a planner. A possibility must become salient and action-guiding for this historically formed agent. Body, habituality, past commitments, culture, and current concerns structure the horizon in which some possibilities appear meaningful and others remain invisible.

```text
generated candidate set
  != lived or functionally integrated practical horizon
```

For AI, a functional analogue would require history-dependent salience, reason-sensitive comparison, persistent commitments, and post-choice self-modification. See [[Practical Alternatives Are Genetically Constituted]], [[Passive Synthesis]], and [[Habituality]].

## Diachronic Profile Without Option Counting

行為時点だけでなく自己形成史に存在した代替を評価する必要がある。

しかし、選択肢の数や人生全体の選択密度を責任の量へ比例させることはできない。

代替の存在、主体による認識、実行可能性、理由応答性、現在の能力形成への寄与、後の改訂可能性を分けて記述する必要がある。

→ [[Diachronic Alternatives Do Not Make Responsibility Proportional to Option Count]]
→ [[franklinNeoFrankfurtiansBufferCases2011]]
