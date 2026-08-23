---
type: concept
status: developing
created: 2026-08-22
updated: 2026-08-22
source: conversation
sourceConversation: "[[2026-08-12-AIへの自由意志と責任の帰属可能性]]"
sourceRange:
  - "chars 0-9936"
  - "chars 9936-21691"
tags:
  - ai-responsibility
  - responsibility-gap
---

# Responsibility Gap

## Core Idea

Responsibility gap is the problem that autonomous or learning artificial systems may produce harmful or illegal outcomes while no human agent appears to have enough knowledge, control, or foreseeability to bear ordinary moral responsibility for the outcome.

In [[matthiasResponsibilityGap2004]], the gap has the following structure:

    Learning AI
        ↓
    Behavior not fully predictable by designer or user
        ↓
    Harmful / illegal outcome
        ↓
    Human actors lack sufficient control or knowledge
        ↓
    AI lacks ordinary moral responsibility
        ↓
    No obvious bearer of responsibility

This is not merely a legal allocation problem. It is also a philosophical problem about whether causal production, control, knowledge, authorship, and blameworthiness can come apart in AI systems.

---

## Four Gaps

[[santoni-de-sioFourResponsibilityGaps2021]] argues that the responsibility gap should be decomposed rather than treated as a single gap.

The relevant distinctions include:

- culpability gap
- moral accountability gap
- public accountability gap
- active responsibility gap

This matters because solving one gap may not solve the others. For example, a company might be legally liable, while no individual is morally blameworthy in the ordinary sense; or a system might be publicly accountable through institutional procedures without being a moral agent.

---

## Is There Really a Gap?

The existence of a genuine responsibility gap is disputed.

[[konigsArtificialIntelligenceResponsibility2022]] asks what exactly the problem is supposed to be. One line of criticism is that AI autonomy does not automatically erase human responsibility. Responsibility can be shifted to design, deployment, oversight, or governance decisions.

[[tigardNoTechnoResponsibilityGap2021]] similarly argues that responsibility practices are more flexible than the strongest gap arguments assume. If responsibility can be assigned for negligence, risk creation, institutional failure, or deployment decisions, then lack of direct control over the final AI output may not create a complete gap.

Thus the key issue is not simply:

> Did the human directly control the AI's final action?

but rather:

> What is the proper object of responsibility: the final action, the deployment decision, the organizational process, the governance failure, or the artificial agent's own agency?

---

## Relation to Free Will

The conversation connects responsibility gap analysis with the distinction:

    Free = Alternative Possibilities
    Will = Sourcehood

This yields a more precise framework.

| Candidate bearer | Alternative Possibilities | Sourcehood | Responsibility status |
|---|---|---|---|
| Developer | Often yes | Partial | Design / training / safety responsibility |
| User | Often yes | Partial to strong | Prompting / misuse / supervision responsibility |
| Organization | Often yes | Possibly collective | Deployment and governance responsibility |
| AI agent | Disputed | Deeply disputed | Central philosophical question |
| Human-AI system | Often yes | Possibly system-level | Hybrid or distributed responsibility |

This table shows why responsibility gap debates cannot be settled only by asking whether an AI caused harm. The crucial question is whether any candidate bearer has the right combination of practical alternatives, sourcehood, epistemic competence, and reasons-responsiveness.

---

## AI Agent as the Hard Case

Current LLM agents may have multiple technically available outputs or action plans. They can sample different responses, call different tools, and pursue different subgoals.

But this does not automatically establish morally relevant [[Alternative Possibilities]]. There is a difference between:

    Multiple possible outputs
        ≠
    Agent-level alternatives owned by the agent as practical possibilities

The deeper difficulty is [[Sourcehood]]. Even if an AI selects an action through reasoning, its goals and evaluative structure are shaped by:

- training data
- RLHF / preference learning
- system prompts
- developer instructions
- tool permissions
- memory architecture
- user instructions
- surrounding institutional context

The AI may be a proximate causal source without being the responsible source of its own will.

---

## Relevance to My Theory

Responsibility gap is the entry point for asking whether AI responsibility can be analyzed through a free-will framework.

My emerging model is:

    Moral Responsibility Candidate
        requires
    Practical Alternative Possibilities
        +
    Frankfurtian Second-Order Volitional Structure
        +
    Diachronic Reflective Sourcehood
        +
    Epistemic and Reasons-Responsive Competence
        +
    Individuated Causal-Historical Continuity

On this model, responsibility gaps arise when no candidate bearer satisfies the relevant responsibility conditions at the required level.

---

## Related Concepts

- [[Alternative Possibilities]]
- [[Agency-Level Alternative Possibilities]]
- [[Sourcehood]]
- [[LLM Sourcehood Problem]]
- [[Artificial Moral Agency]]
- [[Moral Crumple Zone]]
- [[AI Individuation]]
- [[Genetic and Diachronic Agency]]
- [[Individuated Causal-Historical Continuity]]

## Related Arguments

- [[Deployment Responsibility for Unpredictable AI]]
- [[Distributed Responsibility for AI Systems]]
- [[Organizational Responsibility for AI Deployment]]
- [[Alternative Possibilities Alone Are Insufficient for AI Responsibility]]
- [[Frankfurtian Second-Order Volition Does Not Solve AI Sourcehood]]
- [[Free Will Conditions for Artificial Moral Responsibility]]

## Related Literature

- [[matthiasResponsibilityGap2004]]
- [[santoni-de-sioFourResponsibilityGaps2021]]
- [[konigsArtificialIntelligenceResponsibility2022]]
- [[tigardNoTechnoResponsibilityGap2021]]
- [[constantinescuResponsibilityGapsLLMs2025]]
