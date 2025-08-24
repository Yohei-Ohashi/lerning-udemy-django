# uv-on-docker-lab

uvとDockerを使用したPython開発環境のサンプルプロジェクトです。

## 概要

このプロジェクトは、uv（高速なPythonパッケージマネージャー）とDockerを組み合わせて、効率的なPython開発環境を構築する方法を示しています。

## 特徴

- **uv**: 高速なPythonパッケージマネージャー
- **Docker**: コンテナ化された開発環境
- **開発環境**: ホットリロード対応の開発サーバー

## セットアップ

### 前提条件

- Docker
- Docker Compose

### 環境設定

初回セットアップ時は環境変数ファイルを作成してください：

```bash
# .env.exampleをコピーして.envを作成
cp .env.example .env
```

必要に応じて `.env` ファイルの設定を変更してください。
- `JUPYTER_TOKEN`: Jupyter Labのアクセストークン（空なら無認証）

### 起動方法

```bash
# 開発環境を起動
docker-compose up --build

# バックグラウンドで起動
docker-compose up -d --build
```

### 停止方法

```bash
# コンテナを停止
docker-compose down
```

## プロジェクト構造

```
uv-on-docker-lab/
├── app/                 # アプリケーションコード
│   ├── __init__.py
│   └── main.py
├── docker-compose.yml   # Docker Compose設定
├── Dockerfile.dev       # 開発用Dockerfile
├── pyproject.toml       # Pythonプロジェクト設定
├── uv.lock             # uv依存関係ロックファイル
└── README.md           # このファイル
```

## 開発

Jupyter Labは `http://localhost:8888` でアクセスできます。

コードを変更すると、自動的にホットリロードされます。

## ライセンス

MIT License
