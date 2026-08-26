---
type: concept
status: developing
created: 2026-08-23
tags:
  - ai-agents
  - authorization
  - governance
concept_origin: project-working-concept
origin_field: "本研究のagent authorization・監査モデル"
canonical_sources:
  - "[[southAuthenticatedDelegationAuthorized2025]]"
  - "[[otsukaAIIdentityStandards2026]]"
---

# Policy-Attested Agent Authorization

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究で導入した作業概念。
> **概念自体の来歴**：authenticated delegation、AI identity、policy enforcementの既存技術を統合するため、このVaultで導入した作業名称である。
> **本研究で加えた部分**：誰が、どのagentへ、どのpolicyの下で、どの操作を許可したかを検証可能な証明として扱う。
> **主な根拠**：[[southAuthenticatedDelegationAuthorized2025]]、[[otsukaAIIdentityStandards2026]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
> **注意**：この区分は、このVaultで研究用語として導入したことだけを示す。世界初の命名や、先行する同名用法の不存在は主張しない。
<!-- concept-provenance-note:end -->

AIエージェントへAPI権限を発行する際に、適用されるplatform policyのidentityとversionを認証認可記録へ結びつける方式。

## Three Layers

1. platformが署名付きpolicyを配布する。
2. agentは受領したpolicy ID、version、hashをrequestへ添付する。
3. gatewayはattestationを検証し、禁止商品や高リスク操作を決定論的に拒否する。

attestationが証明するのは「正しいpolicyを受領し、特定versionを参照対象として宣言したこと」までである。

agentがpolicyを意味的に理解し、実際の推論で遵守したことまでは証明しない。

この限界があるため、policy promptをsecurity boundaryとして扱わず、tool scope、parameter validation、human approval、deterministic enforcementを併用する。

## Accountability Role

各actionへpolicy versionとauthorization decisionを紐づけることで、事故時に次を区別できる。

- agentが古いpolicyを参照した。
- platformが危険な権限を発行した。
- policyは正しかったがenforcementが欠落した。
- user delegationが許容範囲を超えていた。

## Related

- [[Agentic Causal Provenance]]
- [[Corporate Remedial Responsibility for Agentic AI]]
- [[southAuthenticatedDelegationAuthorized2025]]
