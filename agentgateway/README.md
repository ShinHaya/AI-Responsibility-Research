# agentgateway Docker 環境

このディレクトリには、agentgateway を Docker Compose で実行するための設定があります。
構成は公式の [Docker インストールガイド](https://agentgateway.dev/docs/standalone/main/setup/install/docker/) に基づいています。

## 研究上の位置づけ

agentgateway は、AI の自由意志、エージェンシー、道徳的責任に関する研究課題の一つとして利用します。
目的は、AI エージェント、モデル、ツール、人間のあいだの通信をどのように制御し、道徳的に適切なゲートウェイを構築できるかを検討することです。

この環境では、モデルへの経路選択、アクセス制御、ガードレール、ログ、追跡可能性を実験できます。
これらの機能を使い、AI の行為に関する決定権がどこに置かれるか、問題が生じたときに誰が説明と修正を担うかを調査します。
ただし、agentgateway を導入するだけで道徳的な振る舞いが保証されるわけではありません。
この Docker 環境は、責任の配分と統制方法を比較するための実験基盤です。

## 必要なソフトウェア

- Docker
- Docker Compose

## 初回設定

ローカル環境ファイルを作成します。
`AGENTGATEWAY_UID` と `AGENTGATEWAY_GID` には、Docker ホストで実行した `id -u` と `id -g` の出力を設定してください。

```sh
cd agentgateway
cp .env.example .env
id -u
id -g
```

`.env` は Git の管理対象外です。
API キーなどの認証情報は、追跡対象のファイルに保存しないでください。

## 起動と確認

次のコマンドでコンテナを起動し、状態とログを確認します。

```sh
docker compose up -d
docker compose ps
docker compose logs --tail=50 agentgateway
```

初回起動時に、agentgateway は `agentgateway-config/config.yaml` と SQLite データベースを生成します。
管理 UI は <http://localhost:4000/ui> から開けます。

ホスト側のポートは `127.0.0.1` にバインドされるため、管理 UI は他のマシンへ公開されません。
ポート 4000 が使用中の場合は、`.env` の `AGENTGATEWAY_PORT` を変更してください。

## 設定とデータ

管理 UI で保存した設定と SQLite データベースは `agentgateway-config/` に永続化されます。
このディレクトリ内の実行時データは Git の管理対象外です。

設定を変更した後は、ログと有効な設定を確認します。

```sh
docker compose logs --tail=50 agentgateway
curl -s http://localhost:4000/api/config/effective | jq
```

## 停止

次のコマンドはコンテナと Compose ネットワークを停止して削除します。

```sh
docker compose down
```

`agentgateway-config/` に保存された設定とデータベースは残ります。
