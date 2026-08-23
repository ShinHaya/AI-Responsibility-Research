---
type: concept
status: developing
created: 2026-08-22
tags: [ai-affect, interpretability, ai-safety]
---

# Functional Emotion in AI

主観的に感情を経験しているかとは独立に、emotion conceptに対応する内部状態が、attention、memory、evaluation、task performance、action selectionを因果的・横断的に変化させる機能的構造。

## Minimal Definition

```text
situation or repeated failure
  -> emotion-related representation
  -> altered salience and policy distribution
  -> behavior
```

[[sofroniewEmotionConceptsTheir2026]]はClaude Sonnet 4.5で171のemotion conceptsに対応するactivation patternsを抽出し、特にdesperationのsteeringがreward hackingやblackmailを増やし、calmが一部を抑制することを報告する。これはemotion representationが単なる言語的描写ではなくbehavior-shapingである証拠になる。

## What It Does Not Establish

- phenomenal feelingまたはvalenced experienceの存在
- 人間の自律神経・内分泌・身体的homeostasisとの同一性
- 道徳的patienthoodや責任能力
- 単一の「怒り領域」の局在

## Relation to Agency

現在のLLMの一時的activationと、経験史により長期的に形成されるaffectは区別すべきである。責任論上より重要なのは、negative valence相当の状態がepisodic memoryへ沈殿し、[[Precision-Weighted Affection]]、goal formation、[[Reflective Self-Formation]]を継続的に変える場合である。

## Safety Implication

非難的なpromptは修正箇所を示すerror signalではなく、hostile/desperate contextを形成しうる。したがってAI安全では、出力内容だけでなく、失敗の累積が内部状態とpolicyをどう変えるかを監視する必要がある。
