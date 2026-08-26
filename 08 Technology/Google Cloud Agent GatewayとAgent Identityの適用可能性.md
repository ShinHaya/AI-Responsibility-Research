# Google Cloud Agent GatewayとAgent Identityの適用可能性

## 調査範囲

このノートは、Google CloudのGemini Enterprise Agent Platformが提供するAgent GatewayとAgent Identityを調べ、Mercari Agent Gateway構想へ適用できる範囲を評価する。
調査日は2026年8月26日である。
Agent GatewayとAgent IdentityはGAだが、Agent Identity Auth Manager、Principal Access Boundaryの一部対応、Semantic Governance Policiesなどにはpreviewまたは提供予定の機能が含まれる。

## 結論

Google Cloud Agent Gatewayは、前回調査で中心に置いたApigeeよりもOSS agentgatewayの直接的な比較対象である。
MCP、A2A、REST、gRPCを扱い、agent-to-toolとagent-to-agentの通信へAgent Identityに基づく認可、Model Armor、観測を適用できる。

Agent Identityは、Mercariが管理するGoogle Cloud上のAI agentを識別する基盤として利用できる。
SPIFFE ID、短命なX.509証明書、mTLS、DPoPによって、agent runtimeという実行主体を暗号学的に認証できるためである。

ただし、Agent IdentityだけでMercari構想が必要とするAIの識別を完結できない。
現時点のfirst-class Agent IdentityはAgent RuntimeとGemini Enterpriseを対象とし、利用者が外部事業者から持ち込む任意のAIへMercariが同じ方式でIDを発行する仕組みではない。
また、SPIFFE IDが同定するのはhosted agent resourceであり、model、version、session、memory lineage、delegation、実行ごとの因果的履歴をすべて同定するわけではない。

したがって、Agent Identityは[[AI Individuation]]でいうoperational identityの一項目として採用できる。
Mercari側では、外部AIにも対応するfederated agent identity、利用者の委任、agent version、runtime instance、execution manifest、provenanceを別の識別層として結合する必要がある。

## Agent Gateway

### 役割

Agent GatewayはGemini Enterprise Agent Platformのmanaged networking componentである。
利用者からagent、agentからtool、agentからagentへの通信を一つのpolicy enforcement pointへ集める。

対応protocolはHTTPを基礎とするMCP、A2A、REST、gRPCである。
HTTP trafficは少なくとも安全に終端してroutingし、MCPについてはrequestをparseしてtool名、method、read-only属性を認可条件へ利用できる。

A2Aは対応protocolとして明記されているが、公式概要が説明するprotocol-awareなattribute抽出はMCPに限定されている。
したがって、A2A TaskやAgent Cardをどこまで意味的に処理するかは、実機検証なしにOSS agentgatewayと同等とは判定できない。

### 二つの通信方向

Agent Gatewayには二つのmodeがある。

- **Client-to-Agent**：Cursor、Claude Code、Gemini CLIなどのclientからGoogle Cloud上のagentまたはtoolへのingressを制御する。
- **Agent-to-Anywhere**：Google Cloud上のagentから外部のagent、MCP server、tool、APIへのegressを制御する。

Agent Runtimeは両modeを利用できる。
Gemini EnterpriseはAgent-to-Anywhereだけを利用できる。

Agent Gatewayはregional resourceであり、配置したprojectの範囲でagentic interactionを管理する。
agent、MCP server、endpointはAgent Registryへ登録し、既定では未登録のremote destinationをblockする。

### policy enforcement

Agent GatewayはIdentity-Aware Proxyを既定のenforcement layerとして使用する。
IAPはAgent IdentityをprincipalとしてIAM allow policy、deny policy、Principal Access Boundaryを評価する。

MCP trafficでは、agentごとに特定serverまたはtoolへのaccessを許可し、tool名とread-onlyまたはread-writeの区分を条件にできる。
dry-run modeでは拒否対象をCloud Audit Logsへ記録しながらtrafficを通せるため、policy導入前の影響確認に使える。

Model Armorを接続すると、prompt injection、tool poisoning、sensitive data leakageをinlineで検査できる。
Semantic Governance Policiesは自然言語で文脈依存の制御を表し、危険なtoolの組合せなどを制限する。
Service Extensionsを使えば、custom authorization engineまたはthird-party policy serviceへ判断を委ねられる。

### observabilityとregistry

Agent Gatewayはnetwork layerのtelemetryをCloud Logging、Cloud Trace、Agent Observabilityへ送る。
Agent Registryはagent、MCP server、endpoint、skill、publisherをcatalog化し、Gatewayが認可時に参照するmetadataを保持する。

Registry entryとAgent Identityは別の対象である。
Registryはagentの説明、version、framework、capability、endpointなどを管理し、Agent Identityは実行主体を認証するprincipalである。

## Agent Identity

### 識別対象

Agent Identityは、人間identityやgeneric service accountとは異なるfirst-class IAM principalである。
agentをdeployすると、Google Cloudはhost resourceへ対応する一意なSPIFFE IDとX.509 certificateを割り当てる。

Agent Runtimeの例は次の形式になる。

```text
spiffe://agents.global.org-<ORGANIZATION_ID>.system.id.goog/resources/aiplatform/projects/<PROJECT_NUMBER>/locations/<REGION>/reasoningEngines/<AGENT_ID>
```

IAM policyでは、同じresource pathを持つ`principal://`形式を指定する。
IDはorganizationのtrust domain、hosting service、project、region、agent resourceへ結び付く。

この構造により、「どのorganizationが管理する、どのGoogle Cloud resource上のagentか」を識別できる。
同じservice accountを複数agentが共有する方式より、agent単位のleast privilegeと監査を構成しやすい。

### credentialとattestation

X.509 certificateはGoogle Cloudが自動的に発行して更新し、公式資料では有効期間を24時間としている。
developerは長期service account keyを生成できず、agent identityをimpersonateできない。

AgentはGoogle Cloud APIへmTLSで接続する。
Agent Gatewayの外側へ接続するときはcertificate-bound tokenとDPoPを使い、盗まれたtokenを信頼されたruntime外でreplayしにくくする。

この仕組みが保証するのは、credentialを提示したprocessがGoogle Cloudによってattestされたagent resourceに結び付くことである。
agentが期待された目的を持つこと、modelが改変されていないこと、出力が正しいことまでは保証しない。

### agent自身のauthority

Agent IdentityをIAM principalとしてGoogle Cloud resourceへpermissionを直接付与できる。
IAM allowとdeny、Principal Access Boundary、VPC Service Controlsを使えば、agentが自身のauthorityでaccessできるresourceの上限を定められる。

これはMercari側agentがcatalog検索や一般的なfraud checkを行うような、特定利用者の個人権限を必要としない操作に適する。
agent固有権限と利用者固有権限を同じcredentialへ混ぜずに済む。

### end-user delegation

Agent Identity Auth Managerは、third-party toolへ接続するAPI key、OAuth client credential、end-user OAuth tokenを保管してbrokerする。
three-legged OAuthを使うと、agentは特定利用者の同意を受け、その利用者のauthorityで外部serviceへ接続できる。

監査logにはagent identityとend-user identityの両方を残せる。
Gemini Enterprise connectorと組み合わせる場合、利用者credentialはAuth Managerで暗号化し、Gatewayで復号するため、agent自体へraw credentialを渡さない。

これはMercari構想の「誰のために、どのAIが操作したか」を分離して記録する要件と一致する。
ただし、OAuth consentが存在することはMercari取引への十分な委任を意味しない。
出品公開、価格変更、購入、message送信などのoperation、対象、金額、期限、本人承認をMercari独自のdelegation recordへ残す必要がある。

### 対応runtime

公式IAM資料がfirst-class Agent Identityの対応serviceとして挙げるのは次の二つである。

- Gemini Enterprise Agent Platform Runtime
- Gemini Enterprise

Cloud Run上のDIY agentについて、Agent GatewayのIAM policy資料はservice account-based identityを使うよう説明している。
外部vendorのagentをAgent Registryへ登録することはできても、その登録だけでGoogle managed Agent Identityが付与されるとは確認できない。

この制約はBYOAI構想で大きい。
Claude、ChatGPT、利用者のlocal agent、他cloudのagentをMercariへ接続する場合、Google Agent Identityだけでは共通principalを発行できない。

## Mercari構想への適用評価

### 利用できる範囲

MercariがGoogle Cloud Agent Runtimeにserver-side agentをdeployする構成では、Agent Identityをそのagentのprimary runtime identityにできる。
Mercari Agent GatewayはSPIFFE IDを認証し、IAMまたは外部policy serviceで許可されたtoolだけを公開できる。

この構成で直接得られる機能は次のとおりである。

- agentごとのcryptographic principal
- hosting resourceとorganization trust domainへのbinding
- short-lived certificateと自動更新
- mTLSとDPoPによるcredential replay対策
- agent単位のIAM allow、deny、Principal Access Boundary
- agent identityとend-user identityを分けたaudit log
- user-delegated OAuth credentialのbrokerとrevocation
- Agent Registryによるagent、version、capability、endpointのinventory

### 利用できない範囲

Mercari構想が対象とするAIの識別は、runtime authenticationより広い。
Agent Identityだけでは次の事項を確定できない。

- Google Cloud外で動くBYOAIのidentity
- 同じagent resource内で並行するsessionまたはruntime instance
- model provider、model name、weightsまたはmodel version
- prompt、system instruction、tool set、memory stateを含む実行構成
- agentのcopy、branch、mergeをまたぐcausal-historical continuity
- 利用者が許可したoperation、対象、金額、期間
- 一つのtransactionを起動した具体的なexecution
- agent operator、developer、model provider、end userの責任関係

SPIFFE IDを「責任主体として同一のAIであること」の証明に使うのは範囲を広げすぎる。
resourceをredeployして内部modelやmemoryが変わってもresource URIが維持されるなら、同じSPIFFE IDの下で性質の異なるagentが動き得るためである。

### 推奨する識別model

MercariではAgent Identityを捨てず、複数層の識別modelへ組み込む。

| 識別対象 | 推奨ID | Google Agent Identityの役割 |
| --- | --- | --- |
| 人間の利用者 | Mercari user ID | end-user identityとして関連付ける |
| agent operator | organizationまたはvendor ID | SPIFFE trust domainから一部を検証する |
| agent resource | SPIFFE IDまたは外部agent principal | Google-hosted agentではprimary identityにする |
| agent release | agent definition digest、model version、tool manifest | Registry metadataと別途version固定する |
| runtime instance | instance ID、certificate serial、attestation | SPIFFE credentialの提示主体を記録する |
| session | session ID | Agent Identityとは別に採番する |
| delegation | delegation ID | user、agent、scope、期限、approvalを結ぶ |
| execution | execution IDまたはGateway追跡ID | 一回のcommandと結果を結ぶ |
| transaction | Mercari transaction ID | 業務結果とexecutionを結ぶ |

認可時には少なくとも次の組をpolicy inputにする。

```text
human_principal
+ agent_principal
+ agent_release
+ delegation_id
+ requested_operation
+ target_resource
+ risk_context
```

Google Agent Identityを持つagentでは`agent_principal`へSPIFFE IDを格納する。
外部BYOAIでは、Mercariが信頼するOIDC issuer、workload identity federation、mTLS client certificate、vendor attestationを検証し、同じ内部principal schemaへ正規化する。

### A2A方式への適用

利用者の外部agentがA2AでMercari側agentへ依頼する構成では、二つのagent identityを分ける必要がある。

```text
外部BYOAI principal
  ↓ A2A requestとdelegation
Mercari Agent Gateway
  ↓ policy decision
Mercari server-side agentのSPIFFE ID
  ↓ typed command
Mercari API
```

Google Agent Identityが直接識別するのは、主にMercari server-side agentである。
外部BYOAIのidentityは別のtrust domainから受け取り、Mercariがissuerとattestationを検証しなければならない。

server-side agentが内部APIを呼ぶとき、SPIFFE IDだけを記録すると依頼元が失われる。
外部agent principal、human principal、delegation ID、A2A Task IDをforwardし、server-side agentのSPIFFE IDと同じprovenance eventへ保存する。

## PoCで検証する項目

1. Agent Runtimeへ二つのagentをdeployし、それぞれ異なるSPIFFE IDが発行されることを確認する。
2. Agent Gatewayのdry-runでMCP read-only toolとwrite toolへのpolicy差を記録する。
3. 許可されたagentだけがwrite toolを呼べることを確認する。
4. certificate-bound tokenを別runtimeから再利用できないことを確認する。
5. Auth Managerのthree-legged OAuthでagent identityとuser identityがaudit logに残ることを確認する。
6. external A2A agentを登録した場合に提示されるprincipalとattestationを確認する。
7. Agent Registryのversion metadataとdeploy artifact digestをExecution Manifestへ固定する。
8. SPIFFE ID、user ID、delegation ID、A2A Task ID、Gateway追跡ID、transaction IDを一つのprovenance graphへ接続する。
9. agent resourceをupdateまたはredeployしたとき、SPIFFE IDとcertificateとversion metadataがどう変化するかを確認する。
10. Agent Gatewayからcustom authorization serviceへMercari固有のdelegation contextを渡せることを確認する。

## 判定

Google Cloud Agent GatewayとAgent Identityは、Mercariが管理するserver-side agentの通信制御とoperational identityに適合する。
特に、agent principalとend-user principalの分離、short-lived credential、tool単位のpolicy、audit logは構想に直接利用できる。

一方、外部BYOAIの共通identity、agent version、session、delegation、execution lineageをAgent Identityへ統合することはできない。
Mercari Agent Gatewayでは、Google Agent Identityを一つの信頼できるcredential sourceとして受け入れ、vendor-neutralな内部identity modelとprovenance layerを上位に置く構成が妥当である。

## 関連ノート

- [[主要クラウドとSaaSのAI Agent Gateway比較]]
- [[agentgatewayの目的とデプロイ方式]]
- [[OSS agentgatewayとBYOAI Agent Gateway構想の機能差分]]
- [[AI Individuation]]
- [[Policy-Attested Agent Authorization]]
- [[Agentic Causal Provenance]]

## 公式資料

- [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)
- [Agent Gateway IAM policies overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview)
- [Agent Gateway setup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway)
- [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
- [Agent Registry overview](https://docs.cloud.google.com/agent-registry/overview)
- [Gemini Enterprise Agent Platform agents overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)
- [IAM updates for Agent Identity and Agent Gateway](https://cloud.google.com/blog/products/identity-security/whats-new-in-iam-security-governance-and-runtime-defense)
- [Gemini Enterprise Agent Platform updates](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform)
