# OSS agentgatewayとBYOAI Agent Gateway構想の機能差分

## 調査範囲

このノートは、[[Bring Your Own AIによる倫理的なマーケットプレイス]]で提案するMercari Agent Gatewayと、Linux Foundation配下のOSS agentgatewayを比較する。
両者は名前が似ているが、対象範囲と責任モデルが異なる。

Mercari Agent Gatewayは、利用者の委任から取引結果、異議申立て、救済までを扱うマーケットプレイスの制度とシステムの構想である。
OSS agentgatewayは、HTTP、gRPC、LLM、MCP、A2Aの通信を中継し、認証、認可、経路制御、ガードレール、観測可能性を提供するデータプレーンである。
したがって、OSS agentgatewayは構想の共通入口と実行時制御を担えるが、責任分析に必要なデータモデルと業務手続の全体を提供しない。

調査日は2026年8月26日である。
公式の`main`ドキュメントで機能の現状を確認したうえで、安定版として検証する範囲はagentgateway `v1.4.0`に限定した。
Dockerイメージは`cr.agentgateway.dev/agentgateway:v1.4.0@sha256:771afaf093065477fa296eb90dcb618a0300165f12a32f80bbdd1427fab900ec`である。
コンテナの`--version`出力は`1.4.0`、git revisionは`83c952731ee79b4372e3a031382c4ff419ddfee1`だった。
公式リリース資料も同じタグとcommitを示している。
`latest-dev`でのみ確認できる挙動は、以下の判定根拠に含めない。

## 判定区分

- **実現済み**：v1.4.0の標準機能だけで要件を満たせる。
- **設定または外部連携で実現**：CEL、Webhook、ExtAuthz、ExtProc、OpenTelemetryなどを使えば、agentgateway本体を変更せずに実現できる。
- **独自実装が必要**：マーケットプレイス固有のデータモデル、UI、永続化、評価、業務ワークフローを別途実装する必要がある。
- **要調査**：公式資料と今回の実機確認だけでは要件を満たすか判断できない。

「ログが存在する」と「責任分析に必要な因果関係を復元できる」は別の判定である。
同様に、「利用者を認証できる」「MCPセッションを識別できる」「個別のAI実行を時間を通じて同定できる」も別々に評価する。

## Fit-Gap表

| 構想上の要件                | OSS agentgatewayの対応機能                                                                                           | 判定区分             | 根拠                                                                                                                                                                                                                         | 制約と不足                                                                                     | 次の作業                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 通信プロトコルと共通入口          | HTTPとgRPCの汎用プロキシ、LLMの統一API、MCP、A2A、route、backend                                                                | **実現済み**         | [Introduction](https://agentgateway.dev/docs/standalone/latest/about/introduction/)は通常のAPIとLLM、MCP、A2Aを同じデータプレーンで扱えると説明する。                                                                                                 | Marketplace APIそのものと、許可する業務操作の設計は含まれない。                                                   | Marketplace APIを外部AI専用routeへ分離し、非公式な画面操作を許可しない構成を検証する。                                                           |
| 利用者認証と代理アクセス          | JWT、API key、Basic認証、OIDC、Cross App Access（ID-JAG）、OAuth token exchange                                          | **設定または外部連携で実現** | [Cross App Access](https://agentgateway.dev/docs/standalone/latest/configuration/security/backend-authn/cross-app-access/)は、受信したOIDC ID tokenを主体として下流API用トークンを取得する。                                                        | v1.4.0ではDPoP、`.well-known` discovery、SAMLまたはrefresh token主体を未対応とする。認証は委任内容の理解や本人承認を証明しない。 | Mercari IdPと認可サーバーを用意し、audience、resource、scope、失効時の挙動を統合試験する。                                                    |
| AIサービスおよび個別実行の同定      | API keyまたはJWTのclaim、MCP session ID、ログへのCEL追加項目                                                                  | **独自実装が必要**      | [MCP observability](https://agentgateway.dev/docs/standalone/latest/mcp/mcp-observability/)は`mcp.session.id`を接続単位の識別子として記録する。                                                                                              | session IDはプロトコル上の接続状態であり、AIサービス、モデル版、実行環境、再試行をまたぐoperational agent identityではない。         | Agent、AgentProvider、Execution、ModelVersion、RuntimeEnvironmentを別エンティティとして設計し、署名済みclaimをGateway追跡IDへ結ぶ。            |
| 委任範囲と撤回               | JWT claim、scope、CEL認可、route別policy、rate limit、期限付きトークン                                                          | **設定または外部連携で実現** | [CEL variables](https://agentgateway.dev/docs/standalone/latest/reference/cel/variables/)はJWT、API key、request、metadataを認可規則から参照できる。                                                                                        | 操作、データ範囲、金額上限、有効期間を利用者が理解して設定するUI、委任台帳、即時撤回の伝播はない。                                        | 独立したDelegation Serviceを作り、短命tokenとオンライン失効確認をExtAuthzまたはCELから参照する。                                                |
| サブエージェントへの再委任         | A2A中継、MCP認証認可、JWT claim、trace context                                                                           | **独自実装が必要**      | [Introduction](https://agentgateway.dev/docs/standalone/latest/about/introduction/)はA2A通信を扱うが、通信対応は委任連鎖の意味論を定義しない。                                                                                                         | 親委任から子委任への権限縮小、委任者、受任者、再委任の承認、失効伝播を保持するモデルがない。                                            | Delegation Edgeを設計し、子の権限が親の権限を超えない不変条件を認可サービスで検証する。                                                              |
| 操作認可とリスク別制御           | HTTPとMCP認可、CEL、ExtAuthz、ExtProc、route、rate limit、timeout、retry、direct response                                  | **設定または外部連携で実現** | [Policies](https://agentgateway.dev/docs/standalone/latest/configuration/policies/)と[External authorization](https://agentgateway.dev/docs/standalone/latest/configuration/security/external-authz/)は要求単位の制御点を提供する。        | 取引の影響、金額、個人情報、取り消し可能性を評価する市場固有のrisk engineはない。retryは非冪等な取引操作にそのまま適用できない。                  | Policy Decision ServiceをExtAuthzで接続し、操作別のfail-closed、冪等性key、停止基準を試験する。                                           |
| 利用規約と倫理規則の適用          | CEL、request transformation、LLMとMCP guardrails、regex、外部moderation、custom webhook                                 | **設定または外部連携で実現** | [Guardrails](https://agentgateway.dev/docs/standalone/latest/llm/prompt-guards/)はregex、PII検出、外部安全サービス、custom webhookの多層適用を扱う。                                                                                              | 規約をプロンプトへ入れただけでは理解も遵守も保証しない。曖昧な商品説明、禁止商品の文脈判断、プロンプトインジェクションへの完全な防御も保証しない。                 | 機械判定可能な規則を構造化し、規則ID、判定版、根拠をWebhook応答と監査記録へ残す。                                                                    |
| LLMとMCPの観測可能性         | OpenTelemetryのmetrics、logs、traces、LLMモデルとtoken量、任意のrequest/response capture、MCP method、target、session、tool引数と結果 | **実現済み**         | [LLM observability](https://agentgateway.dev/docs/standalone/latest/llm/observability/)と[MCP observability](https://agentgateway.dev/docs/standalone/latest/mcp/mcp-observability/)が各フィールドとCELによる追加記録を示す。                  | 本文記録は個人情報を増やす。stdout、UI、metrics endpointは証拠保全用の改ざん耐性、暗号化、保存期間、閲覧権限を自動では満たさない。             | 既定では本文を記録せず、必要な項目だけをOpenTelemetry Collector経由で管理された保存先へ送る。                                                       |
| 取引単位のprovenance graph | trace ID、span ID、MCP session ID、CEL metadata、OpenTelemetry export                                               | **独自実装が必要**      | [MCP observability](https://agentgateway.dev/docs/standalone/latest/mcp/mcp-observability/)の例はtrace、span、sessionを記録する。                                                                                                     | traceは通信の親子関係を運ぶが、委任、本人承認、規則判定、取引結果という業務上の因果関係と証拠の確度を表さない。                                | Provenance Serviceを作り、各spanからGateway追跡ID、delegation ID、approval ID、policy decision ID、transaction IDへのedgeを保存する。 |
| プロンプトおよび操作証跡          | LLM requestとresponse capture、MCP tool argumentsとresult、access logのCEL拡張                                         | **設定または外部連携で実現** | [LLM observability](https://agentgateway.dev/docs/standalone/latest/llm/observability/)はpromptとresponseの監査を、[MCP observability](https://agentgateway.dev/docs/standalone/latest/mcp/mcp-observability/)はtool引数と結果の追加を説明する。 | 外部AI内部のsystem prompt、memory、思考過程は観測できない。AI事業者が申告したモデル版や実行環境も暗号学的に検証されない。                  | 観測事実、署名で検証したclaim、自己申告を別フィールドにし、本文の代わりに正規化hashを保存する方針を試す。                                                        |
| データ最小化、保存、削除          | transformation、guardrailによるredaction、OpenTelemetry export、SQLiteまたはPostgresの設定保存                                | **設定または外部連携で実現** | [Transformations](https://agentgateway.dev/docs/standalone/latest/configuration/traffic-management/transformations/)と[Guardrails](https://agentgateway.dev/docs/standalone/latest/llm/prompt-guards/)は送信前の加工点を提供する。        | 証跡の暗号化、法的hold、記録別retention、第三者の閲覧権、削除請求、外部AI事業者側の削除はagentgatewayの責任範囲外である。                | Evidence StoreとPrivacy Serviceを分離し、Execution Manifest、hash、暗号鍵、retention、削除状態を管理する。                              |
| 本人承認と人へのエスカレーション      | ExtAuthzまたはExtProcで要求を保留または拒否し、外部サービスへ判断を委ねられる                                                                  | **独自実装が必要**      | [External processing](https://agentgateway.dev/docs/standalone/latest/configuration/traffic-management/extproc/)は外部処理点を提供する。                                                                                               | 承認内容を理解可能に表示し、修正、拒否、期限切れ、人への引き継ぎを扱うUIと状態機械はない。長時間の人手待ちをgateway接続のまま保持する設計も適切ではない。         | Approval Workflowへ非同期に要求を保存し、承認後に短命のone-time authorizationで再送する。                                                 |
| 異議申立てと救済              | route停止、認可拒否、rate limitなどで被害拡大を抑える制御点                                                                           | **独自実装が必要**      | [Introduction](https://agentgateway.dev/docs/standalone/latest/about/introduction/)が認可、rate limit、timeoutを標準機能として挙げる。                                                                                                      | 取引の一時停止、再審査、当事者への通知、返金、期限管理、判断理由の提示を行うケース管理はない。                                           | Remedy Case Serviceを作り、原因確定前の暫定措置と期限、再審査、返金を取引システムへ接続する。                                                         |
| 市場公正性の測定              | metrics、logs、tracesを評価基盤へexportできる                                                                              | **設定または外部連携で実現** | [LLM observability](https://agentgateway.dev/docs/standalone/latest/llm/observability/)はOpenTelemetry出力を提供する。                                                                                                              | AI利用の有無、AI事業者、料金層ごとの表示、成約、苦情、誤検出の格差を定義し、因果効果を測る機能はない。                                     | Feature Storeと評価pipelineを作り、AI非利用者を含む指標、停止閾値、独立監査用集計を定義する。                                                       |
| 責任区分と事故後の調査支援         | 認証、policy decision、通信ログ、traceが因果調査の入力になる                                                                        | **独自実装が必要**      | [Introduction](https://agentgateway.dev/docs/standalone/latest/about/introduction/)はsecurity、governance、observabilityを提供範囲とする。                                                                                             | 因果的関与、予防義務、救済責任、道徳的責任、法的責任を区別して判断する規則やcase modelはない。ログから責任者を自動決定できない。                     | Case Managementで証拠と判断を分け、各当事者の知識、権限、予見可能性、規則遵守を人が評価できる画面を作る。                                                     |

## 実機で確認した範囲

Docker registryのmanifestから、`v1.4.0`のmulti-platform OCI index digestを確認した。
同じdigestを指定してイメージを取得し、`agentgateway --version`相当の出力から版とgit revisionを確認した。
Composeの構文は固定したイメージ参照を展開できることを確認する。

一方、今回の環境ではLLM provider、MCP backend、OpenTelemetry Collector、外部認可サーバーを接続したend-to-endのfixtureをまだ用意していない。
そのため、trace contextだけで再試行、MCP session、複数のtool call、最終取引結果を一つの業務取引へ結べるかは、未検証である。
公式資料からも業務上のprovenance graphが標準機能として提供されるとは確認できないため、Fit-Gap表では独自実装と判定した。

## メルカリ側AIエージェントを置くA2A方式

### 仮説の構成

外部AIへMarketplace APIを直接公開する代わりに、メルカリ側へA2A Serverとして動くAIエージェントを置く方式が考えられる。
外部AIはagentgatewayを経由してメルカリ側AIへ仕事を依頼し、メルカリ側AIが制限された内部ツールを使って相場調査、出品案の作成、承認要求、取引操作を進める。

```text
利用者
  ↓
外部AI
  ↓ A2A
agentgateway
  ↓
メルカリ側AIエージェント
  ↓ 制限されたツール
認可、本人承認、規則検査
  ↓
メルカリ内部API
```

agentgateway v1.4.0は、A2A listenerからA2A Serverへ要求を中継し、Agent CardのURLを書き換え、`a2a.method`をアクセスログへ記録できる。
したがって、A2Aの通信入口はagentgatewayの標準機能で構成できる。
ただし、agentgatewayがメルカリ側AI、A2A Taskの保存、内部ツール、取引規則、本人承認を生成するわけではない。

### A2A方式で単純になる境界

A2A方式では、外部AIへ商品検索、下書き、公開、価格変更ごとの内部APIを見せず、少数のA2A skillを公開できる。
内部APIを変更してもA2A skillの契約を維持すればよいため、外部AIとの結合も弱められる。

A2AのTaskには一意のID、状態、Message、Artifact、履歴があり、streaming、push notification、cancelも仕様化されている。
この状態モデルは、相場調査、出品案の作成、追加情報の要求、本人確認待ちという複数段階の仕事を一件として扱う場合に適する。

A2A方式は、外部AIへ渡すデータをメルカリ側AIの応答へ限定できる点でも有利である。
しかし、この利点はメルカリ側AIが参照できる内部ツールとデータを狭く制限した場合に限られる。
広い検索権限や汎用的な内部APIを与えれば、外部からのプロンプトインジェクションをメルカリ側AIが内部へ運ぶ危険が残る。

### 移動する複雑さと責任

「外部AIが内部APIを直接呼ばなければ、細かな認可は不要になる」という理解は正しくない。
A2Aはエージェント間の通信とTask lifecycleを標準化するが、利用者が許した操作、データ範囲、金額上限、有効期間を表す委任モデルを提供しないためである。

メルカリ側では、A2A Server、Agent Card、Taskの永続化、再接続、重複通知、期限切れ、モデル、prompt、tool selection、内部ツール、監査を新たに実装する必要がある。
A2A仕様上も、すべてのMessageがTask履歴へ保存されるとは限らず、Messageを重要情報の確実な配送手段として扱うことはできない。
本人承認、規則判定、取引結果は、A2A履歴とは別の証拠記録へ保存する必要がある。

責任の配置も変わる。
直接API方式では外部AIが具体的な操作を要求するが、A2A方式ではメルカリ側AIが利用者の目標を解釈し、操作を計画する。
メルカリ側AIが価格、商品説明、操作順序を決めるほど、モデル選択、tool definition、監督、停止についてメルカリが負う予防上の義務は増える。

この変化は、外部AIの挙動をメルカリが制御可能な内部エージェントで受け止めるという安全上の利点と対になっている。
A2A方式は責任を減らすのではなく、外部AIだけでは制御できなかった判断の一部をメルカリ側へ引き受ける方式である。

### PoCでの方式選択

PoCの目的が、出品支援への需要、作業時間の短縮、本人が許容できる委任範囲を測ることなら、型付けされたコマンドAPIを直接認可する方式が適する。
A2A方式では外部AIの性能に加えてメルカリ側AIの解釈と計画の性能が結果へ混入し、利用されなかった原因を切り分けにくくなるためである。

PoCでは、次のように副作用のない提案と取引操作を分ける。

- `search_market_price`：相場を検索する。
- `create_listing_draft`：出品案を作るが公開しない。
- `request_publish`：具体的な公開内容を本人へ提示する。
- `publish_approved_listing`：署名済みのone-time authorizationがある場合だけ公開する。
- `cancel_request`：未実行の要求を停止する。

この構成なら、各操作の成功、失敗、所要時間、本人の修正、承認、拒否を個別に測定できる。
二重出品、上限外の価格、期限切れ承認も、型、validation、idempotency keyで検査できる。

A2AをPoCへ含めるのは、長時間作業、中断後の再開、作業中の追加質問、進捗通知、複数外部AIとの相互運用性、メルカリ側AIへ相談する体験のいずれかが検証対象である場合に限る。
それ以外ではコマンドAPIから始め、複数段階の仕事への需要を確認した後、そのAPIをメルカリ側A2Aエージェントの内部ツールとして再利用する。

### 現時点の判定

A2A方式は、外部AI向けインターフェースと内部APIの隔離を単純化する。
一方、Mercari Agent Gateway全体の複雑さを減らすとは確認できず、複雑さをメルカリ側AIと安全なツール実行基盤へ移す。

したがって、初期PoCでは型付けされたコマンドAPIを採用し、A2A方式は複数段階のTaskと会話的な協調にPMFが見つかった後の候補とする。
この順序なら、PoCで作った認可、承認、監査、コマンドAPIをA2A方式へ移行しても再利用できる。

## 実装バックログ

### P0 共通入口と認可の最小実証

- **設定**：Marketplace API専用route、JWT検証、操作別CEL、rate limit、timeout、request transformationをv1.4.0で定義する。
- **外部連携**：Delegation ServiceとPolicy Decision ServiceをExtAuthzで接続する。
- **依存関係**：利用者、AIサービス、Execution、操作、データ範囲、金額上限、有効期間の最小schemaを先に決める。
- **検証方法**：期限切れ、撤回済み、上限超過、未登録AI、禁止操作がfail-closedになる統合テストを行う。
- **fork判定**：標準policyとExtAuthzで実現し、agentgateway本体はforkしない。

### P0 Gateway追跡IDと来歴の最小実証

- **データモデル**：GatewayTrace、Delegation、Execution、PolicyDecision、Approval、TransactionResult、EvidenceClaimを別エンティティにする。
- **外部連携**：OpenTelemetry CollectorからProvenance Serviceへspanを送り、業務IDを結ぶ。
- **依存関係**：すべての入口でGateway追跡IDを発行し、非冪等操作にはidempotency keyを必須にする。
- **検証方法**：一件の模擬出品について、指示、AI要求、拒否または承認、公開結果をgraphから再構成する。
- **fork判定**：CEL metadataとheader propagationで必要なIDを運べる限りforkしない。streamingまたはMCPで欠落する場合だけupstreamへの拡張を検討する。

### P0 本人承認と安全な実行

- **APIとUI**：操作、相手への影響、送信データ、金額、取り消し可能性を示し、承認、修正、拒否、人への引き継ぎを受け付ける。
- **ポリシー**：閲覧、下書き、公開、価格変更、メッセージ送信を別のrisk classにする。
- **依存関係**：Delegation Service、Policy Decision Service、one-time authorizationを使う。
- **検証方法**：古い承認、内容変更後の承認、二重送信が実行されないことを確認する。
- **fork判定**：独立したApproval Workflowとして実装し、gateway接続を人手待ちの間は保持しない。

### P1 証拠保全とプライバシー

- **データモデル**：Execution Manifest、content hash、暗号化payload、evidence class、retention、legal hold、deletion requestを定義する。
- **外部連携**：管理されたEvidence Store、鍵管理、監査ログ、外部AI事業者の削除APIを接続する。
- **依存関係**：観測事実、検証済みclaim、自己申告を区別するschemaを使う。
- **検証方法**：低リスク操作では本文を保存せず同一版を照合でき、高リスク記録は権限のない担当者から読めないことを確認する。
- **fork判定**：OpenTelemetryと外部storeで実現し、agentgateway本体はforkしない。

### P1 規則検査とプロンプトインジェクション対策

- **ポリシー**：禁止商品、金額、送信先、個人情報を構造化し、規則IDと版を判定結果へ含める。
- **外部連携**：Guardrails、Webhook、ExtProcを使い、取引本文を権限変更の命令として扱わない検査を行う。
- **依存関係**：誤検出時の再審査と救済を先に定義する。
- **検証方法**：商品説明とメッセージに混入した権限昇格指示、難読化した個人情報、境界値の価格変更をred-team fixtureで試す。
- **fork判定**：外部policy serviceで開始し、一般化できる不足だけをupstreamへ提案する。

### P1 異議申立てと救済

- **ワークフロー**：取引停止、当事者通知、再審査、期限、返金、再開をcase stateとして実装する。
- **監査**：自動判定と人の判断を別記録にし、理由と証拠参照を残す。
- **依存関係**：Transaction Service、Approval Workflow、Provenance Serviceを接続する。
- **検証方法**：原因未確定の模擬事故で被害拡大を止め、売り手と買い手の双方が異議を提出できることを確認する。
- **fork判定**：マーケットプレイス固有の周辺サービスとして実装する。

### P2 市場公正性と運用評価

- **評価**：AI利用有無、AI事業者、料金層別に表示機会、成約率、苦情、出品停止、誤検出、修正率を測る。
- **UI**：運営チームが閾値超過を確認し、権限縮小または実証停止を実行できるようにする。
- **依存関係**：プライバシーを保った集計設計と、AIを使わない対照経路を維持する。
- **検証方法**：事前登録した停止基準を過去データとsynthetic dataへ適用する。
- **fork判定**：評価基盤と運用UIは独立実装とする。

## 後続Issue候補

1. v1.4.0用のMarketplace API routeとJWT、CEL、rate limitの最小設定を追加する。
2. Delegation ServiceのschemaとExtAuthz契約を設計する。
3. OpenTelemetryを使ったGateway追跡IDの伝播とprovenance graphのfixtureを作る。
4. 本人承認のone-time authorizationと冪等な再送APIを実装する。
5. Execution Manifest、hash、暗号化、retention、削除のEvidence Storeを設計する。
6. 規則検査Webhookとプロンプトインジェクションのred-team suiteを作る。
7. 異議申立て、再審査、返金を扱う救済case modelを設計する。
8. AI利用の有無による市場公正性と誤検出率の評価pipelineを設計する。

## 関連ノート

- 技術概要とデプロイ方式：[[agentgatewayの目的とデプロイ方式]]
- 構想の原稿：[[Bring Your Own AIによる倫理的なマーケットプレイス]]
- AIの識別：[[AI Individuation]]
- 因果的な来歴：[[Agentic Causal Provenance]]
- 委任と権限：[[Policy-Attested Agent Authorization]]
- 救済責任：[[Corporate Remedial Responsibility for Agentic AI]]
- 責任の区分：[[Responsibility]]、[[Responsibility Gap]]

## 公式資料

- [agentgateway v1.4.0 release](https://github.com/agentgateway/agentgateway/releases/tag/v1.4.0)
- [Introduction](https://agentgateway.dev/docs/standalone/latest/about/introduction/)
- [LLM observability](https://agentgateway.dev/docs/standalone/latest/llm/observability/)
- [MCP observability](https://agentgateway.dev/docs/standalone/latest/mcp/mcp-observability/)
- [Cross App Access](https://agentgateway.dev/docs/standalone/latest/configuration/security/backend-authn/cross-app-access/)
- [Guardrails](https://agentgateway.dev/docs/standalone/latest/llm/prompt-guards/)
- [CEL variables](https://agentgateway.dev/docs/standalone/latest/reference/cel/variables/)
- [Connect to an agent](https://agentgateway.dev/docs/standalone/latest/agent/a2a/)
- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)
- [A2A specification source](https://github.com/a2aproject/A2A/blob/main/docs/specification.md)
