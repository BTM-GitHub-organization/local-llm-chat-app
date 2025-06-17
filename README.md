# About

このリポジトリは『Mac miniでローカルLLM(LM Studio)動かしてみた』の記事で作成したアプリケーションです。

以下の手順に従って、環境をセットアップしてください。

## 環境構築

### 前提条件

Dockerが動作する環境が準備済みの前提となります。

### 環境構築

Dockerコンテナをビルドします。
```
# docker-compose build
```

Dockerコンテナを立ち上げます。
```
# docker-compose up -d
```

以下にアクセスしてチャット画面が表示されれば環境構築完了です。  

http://localhost:5050/
