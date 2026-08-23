---
type: question
status: open
created: 2026-08-12
---

# Can Distributed AI Be One Responsible Agent?

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：本研究の問いを管理するQuestion Note。問いの設定は研究上の仕事であり、結論が確立していることを意味しない。
> **分析哲学の標準概念**：該当なし。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：[[AI Individuation]]。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Question

複数のAI instanceがmemory、goal、reflection、自己形成結果を継続的に完全共有する場合、それらは複数の主体なのか、一つのdistributed artificial agentなのか？

## Problem

A, B, Cがそれぞれ異なる物理server上で動作していても、

memory(A) = memory(B) = memory(C)

かつgoal形成・reflectionまで同期されているなら、物理instance数を人格数とする理由は弱くなる。

## Hypothesis

AIの個体境界はphysical processではなく、

**causal-historical self-formation boundary**

によって定義すべきかもしれない。

## Responsibility Question

distributed agentが不正を行った場合、

- instance
- model
- collective agent
- deploying organization

のどのlevelへ責任を帰属すべきか？

## Related

- [[AI Individuation]]
- [[Memory Possession Is Not Experience Authorship]]
- [[Free Will Conditions for Artificial Moral Responsibility|Conditions for Artificial Responsible Agency]]
