---
type: concept
status: developing
created: 2026-08-22
source: conversation
sourceConversation: "[[2026-08-12-AIへの自由意志と責任の帰属可能性]]"
sourceRange: "chars 9936-21691"
tags:
  - sourcehood
  - llm
  - ai-responsibility
---

# LLM Sourcehood Problem

## Core Idea

The LLM sourcehood problem is the problem of whether an LLM agent can be the responsible source of its own actions, values, commitments, and second-order volitions rather than merely the proximate causal source of behavior shaped by external training and instructions.

---

## Proximate Source vs Responsible Source

An LLM agent may be the proximate source of an action sequence:

    prompt
        ↓
    planning
        ↓
    tool use
        ↓
    outcome

But responsibility requires more than proximate causation.

The hard question is whether the agent is the source of the practical standpoint from which the action is selected.

    Action
        ← reasons
        ← commitments
        ← values
        ← self-formation history
        ← agent

If the chain terminates in training, RLHF, system prompts, developer constraints, or user goals, then the agent's sourcehood is compromised.

---

## External Goal Problem

A typical LLM agent receives its top-level end from outside:

> Make money.

> Book the trip.

> Complete this task.

Even if it autonomously decomposes that goal into subplans, the most important practical orientation remains heteronomous.

Thus:

    Autonomous execution
        ≠
    Autonomous end-formation

This is why long action chains do not by themselves establish responsible agency.

---

## Relation to Autonomy and Moral Patiency

[[formosaRelationshipAgencyAutonomy2025]] is relevant because it argues that current AI may display sophisticated agency-like behavior while lacking genuine autonomy or agency in a stronger sense.

The cited deficits include externally supplied goals, insufficient self-determination, and lack of critical self-reflection.

These deficits map closely onto the sourcehood problem.

---

## Relation to Frankfurt

Frankfurtian second-order volition improves the model but does not by itself solve sourcehood.

If the system says:

> I want to be moved by legal compliance rather than profit maximization.

we must still ask:

> Is that volition the product of the agent's own reflective self-formation, or merely the developer's policy expressed at a higher level?

---

## Relevance to My Theory

The LLM sourcehood problem motivates a stronger condition:

    Diachronic Reflective Sourcehood
        =
    the agent's evaluative standpoint is formed, revised, retained, and re-opened through its own history of reflection, action, experience, and intersubjective challenge.

This connects sourcehood to:

- [[Reflective Self-Formation]]
- [[Second-Order Volition Requires Open-Ended Revisability]]
- [[Genetic and Diachronic Agency]]
- [[AI Individuation]]
- [[Memory Possession Is Not Experience Authorship]]

---

## Open Questions

- Can sourcehood be functional, or does it require phenomenal selfhood?
- What would count as an AI's own goal formation rather than goal execution?
- Can persistent memory support sourcehood, or does it only store traces of externally driven behavior?
- How can we distinguish genuine self-attribution from generated self-description?
- Is sourcehood possible under fixed safety constraints?

## Related Literature

- [[formosaRelationshipAgencyAutonomy2025]]
- [[keshetSamplingNotChoosing2026]]
- [[calverleyLegalRightsMachines2011]]
- [[martelaArtificialIntelligenceFree2025]]
