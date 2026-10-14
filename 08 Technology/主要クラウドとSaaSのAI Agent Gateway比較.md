# 主要クラウドとSaaSのAI Agent Gateway比較

## 調査範囲

このノートは、AWS、Google Cloud、Microsoft Azureと、主要なSaaSベンダーが提供するAI gatewayをOSS agentgatewayと比較する。
調査日は2026年8月26日である。
各社の機能は更新が速く、previewを含むため、導入時には公式資料で提供地域、service tier、制限を再確認する必要がある。

本ノートでいう**同等性**は、通常のHTTP API、LLM、MCP、A2Aを一つの通信制御層で認証し、認可し、経路制御し、観測できる度合いを指す。
単に複数modelを同じAPIから呼べるサービスは、LLM gatewayとしては近くても、agentgateway全体とは同等と判定しない。

## 調査結果

三大cloudには、agentgatewayと機能が重なるmanaged serviceが存在する。
単一製品として比較できるのはAWSのAmazon Bedrock AgentCore Gateway、Google CloudのGemini Enterprise Agent Platform Agent Gateway、Azure API ManagementのAI gatewayである。

三社以外では、Kong Konnect AI GatewayがLLM、MCP、A2Aを明示的に扱うため、protocol coverageではOSS agentgatewayに最も近い。
PortkeyはLLMとMCPのmanaged gatewayに強く、Cloudflare AI GatewayはglobalなLLM traffic managementに強いが、後者の公式AI Gateway資料はMCPとA2Aのprotocol-aware proxyを中核機能として示していない。

| 提供者 | Managed提供 | HTTP API | LLM | MCP | A2A | OSS agentgatewayとの近さ |
| --- | --- | --- | --- | --- | --- | --- |
| AWS AgentCore Gateway | あり | あり | あり | あり | HTTP targetとして接続可能 | 高い |
| Google Cloud Agent Gateway | あり | あり | model routingが主目的ではない | あり | あり | 高い |
| Azure API Management | あり | あり | あり | あり | あり | 高い |
| Kong Konnect AI Gateway | あり | あり | あり | あり | あり | 最も近い |
| Portkey | あり | LLMとtool接続が中心 | あり | あり | 明示的な専用機能を確認できず | 中程度から高い |
| Cloudflare AI Gateway | あり | LLM endpointが中心 | あり | AI Gateway中核機能として未確認 | AI Gateway中核機能として未確認 | 中程度 |

表の「未確認」は、protocolを通常のHTTPとして通せないという意味ではない。
公式資料から、Agent Cardの書換え、Task metadataの抽出、MCP tool単位の認可といったprotocol-aware機能を確認できなかったことを示す。

## AWS

### Amazon Bedrock AgentCore Gateway

AWSでは、Amazon Bedrock AgentCore Gatewayが最も近いmanaged serviceである。
GatewayはAI agentからtool、他のagent、LLMへの単一の入口を提供し、targetをMCP、HTTP、inferenceの三種類に分類する。

MCP targetでは、Lambda、OpenAPI、Smithy model、remote MCP serverなどをtoolとして公開し、複数targetを一つのvirtual MCP serverへ集約する。
capability synchronization、semantic tool search、target単位のthree-legged OAuthにも対応する。

HTTP targetは、AgentCore Runtime上のagentやA2A serviceを含むHTTP backendへtrafficを直接proxyする。
公式資料はA2Aを接続例として挙げるが、OSS agentgatewayのようなAgent Card URLの書換えやA2A固有telemetryを同じ範囲で説明していない。
したがって、A2A transportは扱える一方、A2A protocol-aware gatewayとしての同等性は限定的である。

Inference targetはmodel名に基づいて複数providerへLLM requestをroutingする。
inbound authorizationにはOAuth JWT、IAM SigV4、認証のみ、開発用の認証なしを選べる。
outbound authorizationにはservice role、caller IAM credential、OAuth client credentials、authorization code、token exchange、token passthrough、API keyを利用できる。

AgentCore PolicyではCedarを使ってGateway toolへの認可規則を記述できる。
AWS IAM、Lambda、Secrets Manager、CloudWatchと統合できる点はmanaged serviceとしての利点である。

### OSS agentgatewayとの差分

AgentCore Gatewayは、AWS上でtoolをMCP化し、agentとmodelを接続する用途ではOSS agentgatewayより構築量を減らせる。
一方、AWS serviceとの統合を前提とするmanaged control planeであり、同じdata planeをlocal binary、VM、Kubernetesへ持ち運ぶOSS agentgatewayのdeployment freedomは持たない。

Mercari Agent Gatewayで利用者ごとのdelegation、本人承認、取引provenance、救済を実装する必要は残る。
OAuth token exchangeやCedar policyは認可の構成要素になるが、marketplace固有の委任意味論を自動的には作らない。

## Google Cloud

### Agent Gateway

Google Cloudでは、Gemini Enterprise Agent PlatformのAgent GatewayがOSS agentgatewayの直接的な比較対象である。
Agent GatewayはMCP、A2A、REST、gRPCを扱い、利用者からagent、agentからtool、agentからagentへの通信を管理する。

Agent Identityを認可principalとしてIAPとIAM policyを適用し、MCP tool名やread-only属性を条件にaccessを制御できる。
Agent Registry、Model Armor、Agent Observability、custom authorization engineとも統合する。

Agent GatewayとAgent IdentityはGoogle Cloud上のagentic communicationを管理する用途に強い。
一方、複数LLM providerへの統一inference API、model routing、semantic cache、token cost管理は主目的ではないため、LLM gatewayとしての機能は別途必要になる。

詳細な適用評価は[[Google Cloud Agent GatewayとAgent Identityの適用可能性]]にまとめる。

### Apigeeと周辺service

Google Cloudでは、Apigeeが既存APIを管理し、agentへtoolとして公開する中心になる。
ApigeeのMCP supportはOpenAPI specificationからmanaged MCP endpointを生成し、`tools/list`と`tools/call`を既存API operationへ変換する。

生成したMCP proxyには、Apigeeの認証、認可、quota、security policy、analyticsを適用できる。
MCP endpointとspecificationはAPI hubへ登録されるため、組織内のtool catalogとして検索できる。

LLM trafficはApigee proxyとApigeeLLM wrapperを使って管理できるが、公式説明ではwrapperの対象がVertex AIとGoogle AI StudioのGemini APIを中心としている。
複数providerを統一APIへ変換する専用LLM gatewayとしては、AWS、Azure、Kong、Portkeyより範囲が狭い。

Model Armorはprompt injection、jailbreak、機密情報、malicious URL、harmful contentを検査するmanaged security serviceである。
Apigeeと組み合わせればguardrailを補えるが、Model Armor自体はroute、backend、MCP session、A2A Taskを管理するgatewayではない。

Google Cloud API GatewayはOpenAPIまたはgRPC定義に基づく通常のmanaged API gatewayである。
AI protocol固有機能を求める場合は、API Gateway単体よりApigeeを評価対象にするほうが適切である。

### OSS agentgatewayとの差分

Agent Gatewayはagent identity、MCP、A2Aとpolicy enforcementの統合により、Apigee単体よりOSS agentgatewayに近い。
ただし、A2AはHTTP trafficとして対応し、公式資料がattribute抽出を明記するのはMCPであるため、A2A固有の観測範囲は実機確認が必要になる。

既存業務APIのMCP化にはApigee、agent通信のpolicy enforcementにはAgent Gateway、prompt securityにはModel Armorという役割分担を取れる。
複数LLM providerの統一routingまで必要なら別のLLM gateway機能を補う。

## Microsoft Azure

### Azure API ManagementのAI gateway

Azureでは、Azure API Managementが既存のAPI gatewayへAI gateway機能を追加している。
通常tierのAI gateway capabilitiesに加えて、modelとMCP toolへ特化したfully managed AI Gateway tierがpublic previewとして提供されている。

AI gatewayはOpenAI Chat Completions、Responses、Anthropic Messages、Google Vertex AIなどのmodel endpointを扱う。
unified model APIは複数backendを一つのOpenAI-compatible endpointへ公開し、形式変換と共通policy適用を行う。

MCPではremote MCP server、OpenAPI specification、built-in connectorを一つのmanaged MCP endpointへ集約できる。
Azureは1,000を超えるSaaS connector、API key、OAuth 2.0、managed identityによるbackend authenticationを説明している。

通常のAPI Management tierでもremote MCP serverを公開し、JWT、Microsoft Entra ID、Azure Monitorを使って認証、認可、観測を行える。
公式資料はA2A agent APIもAI gatewayの管理対象に含めている。

token quota、rate limit、content safety、load balancing、circuit breaker、retry、semantic cache、OpenTelemetryを含むpolicyを利用できる。
Microsoft Foundryと統合すると、model、agent、toolのinventoryとgovernanceを同じcontrol planeから扱える。

### OSS agentgatewayとの差分

Azure API Managementは、managed serviceとしての機能範囲が広く、既存APIとAI trafficを同じ製品で管理する点でOSS agentgatewayに近い。
一方、AI Gateway tierは調査時点でpublic previewであり、提供地域、service limit、pricingが確定していない。

OSS agentgatewayはlocalとKubernetesへ同じRust proxyを配備できるが、Azureのmanaged tierはAzure resource、Entra ID、Azure Monitorなどへ運用を寄せる。
portableなdata planeを優先する場合とAzure運用を統合する場合で選択が分かれる。

## SaaS候補の選定

候補は、managed serviceとして利用できること、複数組織へ提供される製品であること、AI gateway機能が公式資料で確認できることを条件に選んだ。
そのうえで、既存API gateway市場での存在感、global infrastructure、AI gateway専業としての機能幅という異なる種類の影響力を代表するKong、Cloudflare、Portkeyを残した。

この選定は売上またはmarket shareの順位ではない。
非公開情報を推測せず、agentgatewayとの比較に有用な代表三類型を選んだものである。

## Kong Konnect

Kong AI Gatewayは、通常のKong GatewayへLLM、MCP、A2A向けpluginを追加した製品である。
Konnectはそのcontrol plane、analytics、管理UIをSaaSとして提供し、data planeはmanaged cloud、Kubernetes、private environmentなどへ配置できる。

LLMではprovider-agnostic API、credential管理、load balancing、semantic routing、semantic cache、guardrail、token rate limit、usage analyticsを提供する。
MCPではtool trafficの認証、認可、観測を行い、A2Aではrequestを自動識別してTask metadataを抽出し、Agent Card URLを書き換える。

A2A固有のlog、OpenTelemetry span、metricをKonnect analyticsへ送れるため、この部分はOSS agentgatewayと直接比較できる。
通常のAPI gateway機能を同じplugin modelで併用できる点も共通する。

KongはOSS agentgatewayに最も近い商用候補である。
ただし、Kong GatewayのpluginとKonnect control planeへ依存し、OSS agentgatewayのconfigurationやKubernetes CRDとは互換ではない。

## Portkey

PortkeyはLLM gateway、observability、guardrail、prompt管理と、MCP GatewayをSaaSまたはself-hosted形態で提供する。
LLMではuniversal API、conditional routing、fallback、retry、circuit breaker、load balancing、cache、budget、rate limitを利用できる。

MCP Gatewayはclientとserverの間で認証、tool単位のaccess control、credential injection、request loggingを行う。
gateway側のAPI keyまたはexternal IdPと、backend側のOAuth、client credentials、custom headerを分離できる。

per-user OAuth tokenをPortkeyが保持してrefreshし、user identityをbackendへforwardできるため、利用者固有dataへ接続するagentには実用的である。
LLM callとMCP tool callを一つのtraceとdashboardで追える点もSaaSの利点になる。

一方、調査した公式資料ではA2A protocol-aware proxyを確認できなかった。
また、HTTPおよびgRPCの汎用API gatewayを主目的とする製品ではないため、通常APIとA2Aまで同じdata planeで扱うOSS agentgatewayより対象が狭い。

## Cloudflare AI Gateway

Cloudflare AI Gatewayは、複数providerへのmodel requestをCloudflare network経由で管理するSaaSである。
OpenAI-compatible APIと共通REST APIを提供し、provider credentialをCloudflare側へ保管できる。

主な機能はanalytics、requestとresponseのlogging、cache、rate limit、retry、model fallback、dynamic routing、spend limit、guardrail、DLPである。
Cloudflareのglobal networkと既存security serviceを利用できるため、internet-facingなLLM trafficの入口として影響が大きい。

ただし、公式AI Gateway資料が説明する中心対象はmodel inferenceである。
MCP server aggregation、tool単位のauthorization、A2A Agent CardまたはTaskの処理を同じ製品の中核機能として確認できないため、agentgatewayの完全な代替とは評価しない。

Cloudflareは、LLM accessのcost、latency、availability、prompt securityを先に解く場合の候補になる。
Mercari APIのcommand authorizationやA2A gatewayまで求める場合は、別のAPI gatewayまたはagent protocol gatewayを組み合わせる必要がある。

## Mercari Agent Gatewayへの含意

初期PoCでは、cloudまたはSaaSの採用によって独自実装を減らせる範囲と、製品仮説そのものを分ける必要がある。
model routing、MCP変換、JWT検証、rate limit、traceは既製gatewayへ任せられる。

一方、利用者がAIへ何を委任したか、どの操作で本人承認が必要か、取引結果へ誰が異議を申し立てられるかは各社のgatewayが定義しない。
この差はgateway製品の不足ではなく、marketplace applicationが決める業務意味論である。

PoCで型付けされたcommand APIを直接認可するなら、既存のMercari API基盤と統合しやすいgatewayを選ぶほうが検証範囲を小さくできる。
AWS中心ならAgentCore Gateway、Azure中心ならAPI Management、Google Cloud中心ならAgent GatewayとApigeeがmanaged候補になる。
cloud portabilityとlocal検証を優先するならOSS agentgateway、managed control planeとA2Aまで必要ならKong Konnectが比較対象になる。

PortkeyとCloudflareはLLM trafficを中心に始める場合に適する。
Mercariの主要な価値仮説がtool authorizationとtransaction governanceにあるなら、LLM cost optimizationだけで製品を選ばないほうがよい。

## 比較時に残る確認事項

- preview機能の提供地域、SLA、quota、pricingを確認する。
- MCPのprotocol version、Streamable HTTP、session handling、tool filteringの対応範囲を実機で確認する。
- A2Aを通常のHTTPとして通すだけか、Agent Card、Task、telemetryを意味的に扱うかを区別する。
- inbound identityとbackend credentialの対応関係を確認する。
- per-user OAuth token、token exchange、revocation、consentの保存方法を確認する。
- prompt、tool arguments、responseの保存地域、retention、redactionを確認する。
- gateway設定とpolicy decisionをEvidence Storeへexportできるかを確認する。
- non-idempotent commandのretryを停止または制御できるかを確認する。
- vendor lock-inをcontrol plane、policy language、telemetry schema、runtimeの各層で評価する。

## 関連ノート

- [[agentgatewayの目的とデプロイ方式]]
- [[OSS agentgatewayとBYOAI Agent Gateway構想の機能差分]]
- [[Policy-Attested Agent Authorization]]
- [[Agentic Causal Provenance]]

## 公式資料

### AWS

- [Amazon Bedrock AgentCore Gatewayの概念](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html)
- [AgentCore Gatewayの利用方法](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using.html)
- [outbound authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html)
- [AgentCore Policyの概念](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html)

### Google Cloud

- [Google Cloud Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)
- [Google Cloud Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
- [ApigeeのMCP support](https://cloud.google.com/blog/products/ai-machine-learning/mcp-support-for-apigee)
- [Apigee MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart)
- [Model Armor overview](https://docs.cloud.google.com/model-armor/overview)
- [Google Cloud API Gateway](https://docs.cloud.google.com/api-gateway/docs)

### Microsoft Azure

- [Azure API ManagementのAI gateway capabilities](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)
- [AI Gateway tier overview](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview)
- [AI Gateway tierのmodelとtool管理](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-manage-models-tools)
- [MCP server overview](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview)

### SaaS

- [Kong AI Gateway](https://developer.konghq.com/ai-gateway/)
- [Kong A2A Traffic Gateway](https://developer.konghq.com/ai-gateway/a2a/)
- [Portkey AI Gateway](https://portkey.ai/docs/product/ai-gateway)
- [Portkey MCP Gateway](https://portkey.ai/docs/product/mcp-gateway)
- [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/)
- [Cloudflare AI Gateway features](https://developers.cloudflare.com/ai-gateway/features/)
