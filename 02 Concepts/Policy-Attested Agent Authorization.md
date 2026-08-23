---
type: concept
status: developing
created: 2026-08-23
tags:
  - ai-agents
  - authorization
  - governance
---

# Policy-Attested Agent Authorization

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

