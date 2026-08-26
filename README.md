# AI Responsibility Research

AI の自由意志、エージェンシー、道徳的責任を研究するための Obsidian
Vault です。概念、論証、文献ノートを相互にリンクしながら整理しています。

## ディレクトリ構成

- `00 Index/`: MOC、理論マップ、進捗ログ
- `01 Conversations/`: 研究対話の記録
- `02 Concepts/`: 概念ノート
- `03 Arguments/`: 論証ノート
- `04 Literature/`: Zotero と連携した文献ノート
- `05 Questions/`: 研究上の問い
- `06 Theory/`: 理論の統合
- `07 Paper/`: 論文原稿
- `99 Templates/`: Obsidian および文献ノートのテンプレート
- `agentgateway/`: agentgateway の Docker Compose 環境

## agentgateway の起動

Docker と Docker Compose が必要です。初回のみ環境ファイルを作り、`id -u`
と `id -g` の出力に合わせて UID/GID を設定してください。

```sh
cd agentgateway
cp .env.example .env
id -u
id -g
docker compose up -d
```

起動後、<http://localhost:4000/ui> から管理 UI を開けます。詳しい操作方法は
[`agentgateway/README.md`](agentgateway/README.md) を参照してください。

API キー、`agentgateway/.env`、生成された設定ファイルやデータベースは Git
にコミットしないでください。
