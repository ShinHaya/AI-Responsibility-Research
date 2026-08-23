---
type: concept
status: developing
created: 2026-08-23
tags:
  - ai-responsibility
  - ai-agents
  - provenance
---

# Agentic Causal Provenance

AIエージェントの行為について、誰の代理として、どの権限と情報を用い、どの処理を経て結果を生じさせたかを再構成できる記録構造。

単一のagent IDや最終的なtool callだけでは、因果的帰属に必要な情報が不足する。

## Required Relations

- human principalとagent identity
- 委任された権限、範囲、有効期間
- user instructionと参照したlocal instructionのversion
- model、runtime、skill、policyのversion
- retrieval結果、外部観察、sub-agent delegation
- tool call、parameters、authorization decision
- human approval、実行結果、後続の副作用

これらをprovenance graphとして結びつけることで、単一主体への早計な原因帰属を避けられる。

## Privacy Constraint

監査可能性は、参照文書の全文を恒久保存することを意味しない。

低リスク行為ではhashとmetadata、中リスク行為ではredacted excerpt、高リスク行為では閲覧条件を限定したencrypted snapshotを残すなど、リスクに比例した記録が必要になる。

## Epistemic Role

provenanceは責任そのものではない。

しかし、行為者と因果系列を同定できなければ、役割違反、説明義務、企業の救済義務、法的責任を検討できない。

この意味でprovenanceは、上位の責任判断を可能にする認識的基盤である。

さらにprovenanceは、企業がAIへ責任を転嫁するためではなく、被害救済、原因究明、権限停止、再発防止を遂行するために用いられるべきである。

## Execution Trace Is Not Responsibility Provenance

通常のagent observabilityは、model、retriever、tool、responseの実行順序と入出力を記録する。

責任分析には、これに加えて次の関係が必要になる。

- 誰がどのagentへ権限を委任したか。
- 承認が一括、個別、編集後、拒否後の再実行のどれだったか。
- どのpolicy versionに基づきauthorizationされたか。
- local contextのどの部分がplatform actionへ影響したか。
- platform側のenforcementがどこで適用または欠落したか。

したがって既存traceはprovenanceの入力に使えるが、責任帰属を目的としたprovenanceをそのまま提供しない。

platformは自身が観察したAPI requestとauthorization decisionを改ざん耐性のある記録として保持し、local contextについては署名付きmanifest、redacted excerpt、条件付き提出を組み合わせる必要がある。

## Related

- [[AI Individuation]]
- [[Responsibility]]
- [[Attributable Causation Is an Epistemic Precondition for Higher Responsibility]]
- [[southAuthenticatedDelegationAuthorized2025]]
- [[nianAuditableAgents2026]]
- [[huResponsibleAgenticAI2026]]
- [[otsukaAIIdentityStandards2026]]
- [[Corporate Remedial Responsibility for Agentic AI]]
- [[Policy-Attested Agent Authorization]]
