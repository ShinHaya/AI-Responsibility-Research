---
type: concept
status: developing
created: 2026-08-23
tags:
  - ai-responsibility
  - ai-agents
  - provenance
concept_origin: project-extension
origin_field: "agentic AI監査・データprovenance"
canonical_sources:
  - "[[huResponsibleAgenticAI2026]]"
  - "[[nianAuditableAgents2026]]"
  - "[[southAuthenticatedDelegationAuthorized2025]]"
---

# Agentic Causal Provenance

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究による再構成。
> **概念自体の来歴**：AI agentのprovenance、auditability、authenticated delegationに関する既存研究を基礎とする。
> **本研究で加えた部分**：因果系列の同定を上位責任判断の認識的前提として整理し、観測・検証・自己申告の証拠水準を区別する。
> **主な根拠**：[[huResponsibleAgenticAI2026]]、[[nianAuditableAgents2026]]、[[southAuthenticatedDelegationAuthorized2025]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

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
