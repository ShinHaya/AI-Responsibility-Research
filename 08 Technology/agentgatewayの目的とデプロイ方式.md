# agentgatewayの目的とデプロイ方式

## 調査範囲

このノートは、OSS agentgatewayの目的、共通機能、Standalone方式、Kubernetes方式を整理する。
調査日は2026年8月26日である。
公式ドキュメントの`latest`は調査時点で1.4系を指していたため、版に依存する判断では[[OSS agentgatewayとBYOAI Agent Gateway構想の機能差分]]に記録したv1.4.0のリリース情報と照合する。

## agentgatewayの目的

agentgatewayは、通常のHTTPおよびgRPC通信と、LLM、MCP、A2Aの通信を同じデータプレーンで扱うオープンソースのgatewayである。
Linux Foundation配下で開発され、Rust製のproxyがクライアントとバックエンドの間に入り、経路選択、認証、認可、通信制御、観測を行う。

従来のAPI gatewayは、短時間で完了するHTTP requestとresponseを主な対象としてきた。
これに対してMCPはsessionを持つ双方向通信、A2Aは長時間のTask、LLMはprovider固有のAPIとstreamingを含むため、通信の意味を認識した中継が必要になる。
agentgatewayは、通常のAPI gateway機能へLLM、MCP、A2A固有の処理を加えることで、この差を埋める。

agentgatewayはAIエージェントそのものではない。
利用者の目標を解釈して計画を立てたり、Marketplace固有の委任、本人承認、異議申立て、救済を実装したりする製品でもない。
agentgatewayが提供するのは、そうしたアプリケーションを安全に接続し、通信へ規則を適用する実行基盤である。

## 両方式に共通するデータプレーン

Standalone方式とKubernetes方式は、設定の管理方法が異なる一方、通信を処理するagentgateway proxyを共有する。
Kubernetesの公式Architectureも、local configurationとxDS configurationが同じin-memory internal representationへ変換されると説明している。

```text
クライアント
  ↓
listenerとroute
  ↓
policy
  ↓
agentgateway proxy
  ↓
HTTP、gRPC、LLM、MCP、A2Aのbackend
```

### 通常のHTTPとgRPC

agentgatewayは、HTTPおよびgRPCの汎用proxyとして、listener、route、backendを構成できる。
request matching、header操作、redirect、rewrite、body buffering、transformation、traffic splittingにも対応する。
この機能により、通常の業務APIとAI向け通信へ同じ制御方式を適用できる。

### LLM gateway

LLM通信では、複数providerを統一的なAPIの背後へ置き、model名やproviderに応じて経路を選択できる。
OpenAI、Anthropic、Azure OpenAI、Amazon Bedrock、Geminiを含むproviderへ接続し、Chat Completions、Responses、Messages、Embeddingsなどをproviderの対応範囲に応じて扱う。

LLM固有の機能には、virtual model、複数providerへのrouting、request transformation、virtual API key、model cost、budgetおよびspend limitがある。
Guardrailsでは、正規表現、PII検出、外部moderation service、custom webhookをrequestまたはresponseへ適用できる。

### MCP gateway

MCP通信では、stdio、SSE、Streamable HTTPのserverを接続できる。
複数のMCP serverを一つのvirtual MCP endpointへ集約し、利用者ごとに見せるtoolを制限できる。
OpenAPIで記述された既存APIをMCP toolとして公開する構成も取れる。

MCP固有の認証と認可では、OAuth 2.0、JWT、toolまたはmethod単位のCEL規則を利用できる。
MCP session ID、method、target、resource、tool名をログへ出し、必要に応じてtool arguments、result、errorをCELで追加できる。

### A2A gateway

A2A通信では、外部のA2A clientからA2A Serverへrequestを中継する。
agentgatewayはA2A routeを識別し、backend Agent CardのURLをgatewayの公開URLへ書き換え、`a2a.method`をアクセスログへ記録する。

この対応は、Agent Card、Task、Message、Artifactを処理するA2A Serverをagentgatewayが生成するという意味ではない。
A2A ServerとTaskの永続化は、接続先のAIエージェント側で実装する。

### セキュリティ

共通のセキュリティ機能には、TLS、backend TLS、JWT、API key、Basic認証、OIDC browser認証、HTTP認可、network認可、MCP認証認可、外部認可がある。
HTTPおよびMCPの認可規則にはCELを使い、JWT claim、API key、request、backend、MCP情報などを条件として参照できる。

ExtAuthzを使えば、OPAや業務固有のPolicy Decision Serviceへ認可判断を委ねられる。
ExtProcを使えば、外部処理serviceでrequestとresponseを検査または変換できる。
backend authenticationでは、受信したcredentialを下流用tokenへ交換するOAuth token exchangeやCross App Accessを構成できる。

これらの機能は通信要求を許可または拒否する制御点を提供するが、利用者がAIへ与えた委任を自動的に意味づけない。
操作、データ範囲、金額上限、有効期間を扱うには、別の委任モデルと認可serviceが必要になる。

### 通信制御と耐障害性

routeとbackendには、load balancing、timeout、retry、rate limit、mirroringなどを適用できる。
ただし、retryを出品公開や決済のような非冪等操作へ使う場合は、重複実行を防ぐidempotency keyが別途必要になる。

policyは通信を操作、保護、観測する設定であり、適用先と条件を持つ。
CELの条件によって同じrouteへ異なるpolicy variantを適用できるため、主体、操作、risk classに応じた制御へ利用できる。

### 観測可能性

agentgatewayは、metrics、structured logs、distributed tracesを出力する。
OpenTelemetryを使って外部collectorへ送り、Prometheus、Grafana、Loki、Tempo、JaegerやLLM観測serviceと組み合わせられる。

LLM通信ではprovider、request model、response model、token usage、cost、必要に応じてpromptとresponseを記録できる。
MCP通信ではsession、method、target、resource、tool callを記録できる。

ログとtraceが存在することは、業務上のprovenance graphが存在することと同じではない。
委任、本人承認、policy decision、取引結果を因果関係として結ぶには、Gateway追跡IDと外部のEvidence Storeが必要になる。

## Standalone方式

### 構成

Standalone方式では、一つのagentgateway binaryまたはcontainerを起動し、YAMLまたはJSONのlocal configurationで設定する。
設定はgateways、listeners、routes、backends、policiesと、process全体へ適用する`config`に分かれる。

local configurationは監視され、route、backend、policyなどの多くはfile変更後に動的にreloadされる。
DNS、admin、network、observability、session管理など、一部の`config`項目は起動時に固定される。

管理UIから設定を作成し、SQLiteまたはPostgreSQLへ保存する構成も取れる。
ただし、UIと設定databaseは責任分析用の証拠保全基盤ではなく、権限、保存期間、改ざん耐性を別途設計する必要がある。

### 配備方法

Standalone binaryはbare metal、VM、local machineで実行できる。
公式にはbinary、Docker、Standalone用Helm chartによる配備方法が用意されている。
Kubernetes cluster上でStandalone binaryを動かすこともできるが、Kubernetes方式のcontrol planeを利用しない限り、設定管理はlocal configurationのままである。

### 適する場面

Standalone方式は、PoC、local development、単一環境、小規模な配備、設定内容を直接確認したい実験に適する。
一つの設定fileから通信経路とpolicyを追えるため、agentgatewayの挙動を学ぶ段階でも扱いやすい。

一方、複数proxyの設定同期、Kubernetes Serviceのendpoint discovery、Gateway API resourceのstatus、宣言的な権限分離は自動では得られない。
高可用構成にする場合は、processの複製、設定配布、service discovery、secret管理、更新手順を運用側で補う。

## Kubernetes方式

### control planeとdata plane

Kubernetes方式は、agentgateway proxyに加えて、Kubernetes resourceを監視するcontrol planeを使用する。
control planeはGateway API resourceとagentgateway独自resourceを内部設定へ変換し、xDSのstreaming gRPCで各proxyへdelta updateを配布する。

`agentgateway` GatewayClassを使うGatewayを作成すると、deployerが対応するproxyを標準ではDeploymentとして作成する。
AgentgatewayParametersを使えば、image、logging、resource、DeploymentまたはDaemonSetといったworkload設定を変更できる。

control planeは受理または拒否した設定をGateway、listener、routeのstatusへ書き戻す。
無効な設定があっても、他の有効な設定を継続して配布できる。

### Kubernetes resource

標準のGateway APIでは、GatewayClass、Gateway、HTTPRoute、GRPCRoute、TCPRoute、TLSRouteを使う。
agentgateway固有の機能は、主に次のcustom resourceで表す。

- **AgentgatewayBackend**：LLM provider、MCP server、A2A serverなど、標準Service参照だけでは表せないbackendを定義する。
- **AgentgatewayPolicy**：traffic manipulation、security、resiliency、observabilityをGatewayやrouteなどへ適用する。
- **AgentgatewayParameters**：control planeが作成するproxy workloadを調整する。
- **AgentgatewayModel**：localまたはcluster内のmodel routingを高水準に記述する実験的APIである。

Kubernetes Gateway APIが提供するportableな機能で足りる場合は、標準APIを優先できる。
CEL transformation、拡張されたExtAuthz、mTLS、MCPなどが必要な場合はAgentgatewayPolicyを使う。

### Gateway APIとの関係

Gateway APIは、KubernetesにおけるL4およびL7 routingの標準resourceである。
agentgatewayはcoreとextended featureを実装し、標準にないMCPや高度なpolicyをextensionとして加える。

標準APIを使う利点は、他のGateway API implementationへ移行しやすいことである。
agentgateway extensionを使う利点は、CEL、MCP、LLM、A2Aを含む固有機能を一貫したresourceで扱えることである。
設計時には、portableである必要があるrouteと、agentgateway固有機能へ依存してよいpolicyを分ける。

### service discoveryと設定配布

control planeはService、workload、ReferenceGrant、Secretを監視し、endpoint addressを解決する。
関連resourceだけを再計算し、変更のあった設定だけをproxyへ送る。
各proxyは自分のGatewayに必要な設定と共有addressを購読し、受け取った更新をin-memory representationへatomicに適用する。

この構造は、proxy数、route数、backend数が増える環境で設定の一貫性を保ちやすい。
一方、Kubernetes API、CRD、controller、xDS、RBAC、certificate、upgradeという運用対象が増える。

### 導入と運用

公式にはHelm、Argo CD、Flux CDによる導入経路が用意されている。
control planeとproxy間のxDS通信はKubernetes service account tokenで認証でき、TLSで保護できる。

観測ではdata planeの通信metricsとtraceに加え、control plane metrics、proxyが設定を拒否したNACK、Kubernetes eventを監視する。
Admin UIからproxyが実際に受け取った設定を調べることもできる。

### 適する場面

Kubernetes方式は、複数teamが多数のrouteとbackendを運用する環境、proxyを水平拡張する環境、GitOpsとKubernetes RBACを利用する環境に適する。
Service discovery、宣言的設定、status、workload lifecycleをKubernetesへ統合できるためである。

PoCや単一proxyだけの実験では、control planeとCRDの導入が検証対象を増やす場合がある。
Kubernetes固有のscalability、multi-tenancy、Gateway API運用を検証しないPoCでは、Standalone方式から始めるほうが原因を切り分けやすい。

## Standalone方式とKubernetes方式の比較

| 比較項目 | Standalone方式 | Kubernetes方式 |
| --- | --- | --- |
| 通信処理 | 共通のagentgateway proxy | 共通のagentgateway proxy |
| 設定source | local YAMLまたはJSON、UI、SQLiteまたはPostgreSQL | Gateway API、CRD、Service、Secret |
| 設定配布 | file watchとlocal reload | control planeからxDS delta update |
| proxy lifecycle | systemd、Docker、Helmなどを運用者が管理 | deployerがGatewayごとにDeploymentまたはDaemonSetを管理 |
| service discovery | DNSまたは明示したbackend | Serviceとworkloadをcontrol planeが解決 |
| policy表現 | listener、route、backendへ直接設定 | AgentgatewayPolicyをresourceへattach |
| 状態確認 | logs、metrics、UI、effective config | Kubernetes status、event、NACK、metrics、UI |
| 権限分離 | host、file、databaseの権限に依存 | namespace、RBAC、ReferenceGrantを利用できる |
| 更新方法 | binaryまたはcontainerと設定を直接更新 | HelmまたはGitOpsでcontroller、CRD、proxyを更新 |
| 運用負荷 | 小さい構成では低い | 小さい構成では高いが、大規模構成を標準化しやすい |
| 主な用途 | local開発、PoC、単一gateway、小規模配備 | production、複数gateway、multi-team、水平拡張 |

## 方式選択の基準

Mercari Agent Gatewayの初期PoCでは、Standalone方式を第一候補とする。
検証対象が型付けされたコマンドAPI、委任、本人承認、ログ、PMFであり、Kubernetes control planeの運用性ではないためである。

Standalone方式で作ったroute、backend、policyの考え方は、Kubernetes方式でも同じdata planeへ適用できる。
ただし、設定fileをCRDへ機械的に置き換えられるとは限らないため、移行時には標準Gateway APIで表す部分とAgentgatewayPolicyへ置く部分を分ける。

production候補の評価では、次の条件が生じた時点でKubernetes方式を検討する。

- proxyを複数replicaまたは複数Gatewayへ増やす。
- 複数teamがrouteとpolicyを分担する。
- Kubernetes Service discoveryとSecret管理を利用する。
- GitOpsによるreview、rollout、rollbackを必要とする。
- Gateway API resourceのstatusとRBACを運用へ組み込む。
- local LLM workloadへのInference Extension routingを検証する。

## 本研究で区別する事項

agentgatewayの機能評価では、次の対象を同一視しない。

- 認証された利用者と、利用者からAIへの委任。
- MCP session IDまたはA2A Task IDと、時間を通じたAI実行の同一性。
- traceの親子関係と、委任から取引結果までを結ぶprovenance graph。
- promptまたはtool callのログと、改ざん耐性を持つ監査証拠。
- guardrailの検出結果と、規則違反が存在しないという保証。
- gatewayの可用性と、被害を受けた利用者への救済。

## 関連ノート

- [[OSS agentgatewayとBYOAI Agent Gateway構想の機能差分]]
- [[Bring Your Own AIによる倫理的なマーケットプレイス]]
- [[Policy-Attested Agent Authorization]]
- [[Agentic Causal Provenance]]
- [[AI Individuation]]

## 公式資料

### 共通機能とStandalone

- [Standalone Introduction](https://agentgateway.dev/docs/standalone/latest/about/introduction/)
- [Standalone Architecture](https://agentgateway.dev/docs/standalone/latest/about/architecture/)
- [Configuration](https://agentgateway.dev/docs/standalone/latest/configuration/)
- [Policies](https://agentgateway.dev/docs/standalone/latest/configuration/policies/)
- [Security](https://agentgateway.dev/docs/standalone/latest/configuration/security/)
- [LLM observability](https://agentgateway.dev/docs/standalone/latest/llm/observability/)
- [MCP observability](https://agentgateway.dev/docs/standalone/latest/mcp/mcp-observability/)
- [A2A connection](https://agentgateway.dev/docs/standalone/latest/agent/a2a/)
- [Static configuration](https://agentgateway.dev/docs/standalone/latest/configuration/static-configuration/)

### Kubernetes

- [Kubernetes overview](https://agentgateway.dev/docs/kubernetes/latest/about/overview/)
- [Kubernetes architecture](https://agentgateway.dev/docs/kubernetes/latest/about/architecture/)
- [Gateway API](https://agentgateway.dev/docs/kubernetes/latest/about/gateway-api/)
- [Kubernetes policies](https://agentgateway.dev/docs/kubernetes/latest/about/policies/)
- [Install](https://agentgateway.dev/docs/kubernetes/latest/install/)
- [Observability](https://agentgateway.dev/docs/kubernetes/latest/observability/)
- [AgentgatewayPolicy reference](https://agentgateway.dev/docs/kubernetes/latest/reference/api-kubespec/policies/)
- [Kubernetes API reference](https://agentgateway.dev/docs/kubernetes/latest/reference/api/)
