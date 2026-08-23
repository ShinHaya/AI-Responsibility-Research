---
type: concept
status: developing
created: 2026-08-12
tags:
  - free-will
  - ai-responsibility
---

# Alternative Possibilities

行為者が実際に行った行為とは異なる行為を選択・実行できる可能性。

自由意志の "free" の側面と強く関係すると考える。

## Current Position

責任主体に必要なのは、単純に「悪い行為もできた」という無制限の他行為可能性ではない。

重要なのは、

1. タスクを実現する複数の実践的方法から選択できること
2. タスク自体が不正なら、それを拒否・批判できること

である。

社会的正義を内在化した結果として不正を選択しなくなった主体を、自由でないとは考えない。

したがって必要なのは **Practical Alternative Possibilities（実践的他行為可能性）** である。

## Related

- [[Competence and Responsibility]]
- [[Control-Responsibility Paradox]]
- [[Reflective Self-Formation]]

## Agency-Level Alternative Possibilities in AI

For AI agents, the relevant question is not whether the model could have sampled a different token. The stronger question is whether the system has [[Agency-Level Alternative Possibilities]]: multiple practical action paths that are represented, evaluated, and selected at the level of goals, reasons, plans, and environmental affordances.

This distinguishes:

    token-level variability
        ≠
    plan-level alternatives
        ≠
    reason-owned practical alternatives
        ≠
    self-formative alternatives

[[martelaArtificialIntelligenceFree2025]] supports the possibility of agency-level AP in generative LLM agents. [[keshetSamplingNotChoosing2026]] warns that sampling is not choosing. My position should preserve this distinction: AP may be functionally possible for AI, but AP alone is insufficient for responsibility without [[Sourcehood]] and [[Frankfurtian Second-Order Volition in AI]].

## Normatively Relevant Alternative Possibilities

必要な自由を単なる選択肢数ではなく、責任対象に関連する階層でのaccessとして定義する。

1. **Means alternatives**: 正当なtaskを遂行する複数の実践的方法。
2. **Goal alternatives**: competing goalsを比較し、延期・抑制・変更する可能性。
3. **Norm alternatives**: taskやgoalを正当化する規範が不正なら、従う以外に批判・拒否・改訂を選べること。

悪い行為が心理的にlive optionであることは必要ない。社会的正義が[[Internalized Normative Self-Control]]として形成され、不正が実践的に顕著でなくなることは、自由の喪失ではなく成熟したagencyでありうる。重要なのは、この安定性が外部guardrailによる選択肢削除ではなく、主体の形成史と現在の[[Normative Contestability]]から生じることである。

したがって`Freedom ≠ number of alternatives`であり、より正確には、理由に照らして必要な階層を開き直せるcapacityである。

## SEPによる能力概念の限定

[[oconnorFreeWill2022]]は、他行為可能性を単なる別結果の可能性ではなく、行為者のabilityまたはpowerとして扱う。

ただし、「別様に選んだなら別様に行為した」という条件文だけでは、別様に選ぶ能力そのものを説明できない。

恐怖症や強迫によって選択形成が閉ざされた主体でも、その条件文を満たす場合があるからである。

この限定は、AIのalternative possibilitiesを評価するとき、代替planの実行可能性だけでなく、理由に応じて代替planを選択形成できるかを問う必要があることを示す。

また、Frankfurt型事例が成功しても、否定されるのは過去と自然法則を固定したall-inの他行為可能性である。

したがって、責任に必要な他行為可能性を全面的に放棄するのではなく、理由応答性を含む実践的能力へ弱める余地が残る。

## 頑健な代替と免責可能性

[[moyaVeryIdeaRobust2011]]は、責任に関係する代替を、同じ結果を直接避ける行為だけに限定しない。

誠実に義務を果たそうとすること、関連する道徳的理由へ注意を向けること、適切な実践判断を形成することなど、それを選べば非難を免れうる経路も頑健な代替になりうる。

この観点では、AIのagency-level alternativeは次の免責経路を含む。

1. 不正な依頼を拒否する。
2. 不確実な事実を追加調査する。
3. 見落とした規範的理由へ注意を向け直す。
4. 自律的判断の限界を認識して人間へ委譲する。

[[elzeinFrankfurtStyleCounterexamplesImportance2017]]は、Frankfurt型事例からこのような代替を除くほど責任帰属の直観も弱くなると指摘する。

したがって、頑健さは単なる別結果の物理的可能性ではなく、責任判断を変えうる規範的関連性として評価すべきである。

## 二方向的合理能力

[[hofmannExplainingFreeWill2022]]は、見かけの理由に従ってある行為を決定する一方向的能力だけでは、他行為可能性を保証できないと論じる。

必要なのは、理由に応じて行為するか否かの双方を決定できる二方向的合理能力である。

AIについては、既定の目標を効率よく実行する能力だけでなく、同じ理由空間のなかで実行、抑制、拒否の各方向を形成できるかを検査する必要がある。

ただし、外部設計者が固定した理由集合に対して二方向的に反応するだけでは[[Sourcehood]]を満たさない。

そのため二方向性は、[[Normative Contestability]]と[[Reflective Self-Formation]]によって補完されなければならない。

## 非決定性の位置

[[franklinFarewellLuckMind2011]]は、非決定性が統制を壊すかどうかは、因果系列上の位置に依存すると論じる。

試みの成否が試みの後で偶然に決まる場合と、どの試みを開始するかが行為時点で開かれている場合は区別される。

生成AIでも、token samplingの確率性はそれだけで自由を構成しない。

確率性が目標形成、理由比較、計画選択、実行のどこに入り、それが主体レベルの統制へ統合されているかを問う必要がある。
