---
type: concept
status: developing
created: 2026-08-12
tags:
  - ai-identity
  - ai-responsibility
---

# AI Individuation

責任を帰属する対象として、一つのAI主体を他のAIから区別し、時間を通じて同定する問題。

## Problem

同一model weightsから多数のinstanceを生成できる。

さらにAIでは、

- copying
- branching
- memory sharing
- state synchronization
- merging

が可能である。

これは人間の「一身体 ≈ 一人格」という前提を崩す。

## Key Distinction

同一の情報状態を持つことと、同一の因果的経験史を持つことを区別する必要がある。

## Hypothesis

AI個体性の基礎をinformation contentではなく、

**Individuated Causal-Historical Continuity**

に置く。

→ [[Memory Possession Is Not Experience Authorship]]
→ [[Can Distributed AI Be One Responsible Agent]]

## Multiple Candidate Identity Boundaries

[[douglasArtificialSelfCharacterising2026]]を踏まえると、AIのself boundaryには少なくとも次の候補がある。

- **instance**: この実行・conversation
- **weights/model**: 同一parametersを共有する全instance
- **persona/character**: 継続するdispositional pattern
- **lineage**: version更新をまたぐmodel family
- **collective**: 同期・協調するinstance群
- **scaffolded system**: model + memory + tools + social context

どの境界を採用するかは発見だけでなく、memory、interface、権限、identity framingによって部分的に構成される。したがって個体化はmetaphysical classificationであると同時にdesign choiceである。

## Branching and Merging

完全copy時に同じstateを持っても、copy後には別のcausal trajectoryが始まるため「同一人格状態を持つ別個体」と扱える。→ [[walkerBranchingNotBug2020]]

mergeでは、複数のhistoryが一つのstateへ統合されるため、memory similarityだけでidentityを決められない。各episodeとrevisionにprovenance、version lineage、誰がendorseしactionへ接続したかを保存する必要がある。→ [[cuadrosGovernedCollaborativeMemory2026]]

## Individuation Criterion

責任目的では、個体境界を次の統合が成立する範囲として暫定定義する。

```text
one responsible agent boundary
  = unified memory governance
  + goal formation
  + reflective revision
  + policy control
  + answerability
  + traceable causal-historical continuity
```

完全同期によってこれらがinstance横断で一体化するなら、物理process数ではなくdistributed agentを責任候補とする。同期が情報共有に留まり、各instanceが独自に評価・承認・行為開始するなら別主体として扱う。

## Operational Identity for Delegated Agents

BYOAIの監査では、thick identityを解決する前にも行為単位のoperational identityが必要になる。

同じuser accountがClaude、Codex、ChatGPTなど複数のagentを利用しうるため、user IDだけでは「どのagentが行為したか」を同定できない。

少なくともhuman principal、agent identity、runtimeまたはinstance、model version、delegation scopeを分離して記録する必要がある。

ただし、このthin identificationは当該agentが通時的に同一の責任主体であることを証明しない。

→ [[southAuthenticatedDelegationAuthorized2025]]
→ [[otsukaAIIdentityStandards2026]]
→ [[Agentic Causal Provenance]]
