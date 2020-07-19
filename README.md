# README

## 概要

* github pagesとnetlifyで同じものをデプロイする

## セットアップ

サイト作成

```shell
hugo new site heartfulmoon.github.io
```

レポジトリ初期化

```shell
cd heartfulmoon.github.io
git init
echo '*~' >> .gitignore
echo '*.bak' >> .gitignore
echo '*.orig' >> .gitignore
echo '.env' >> .gitignore
echo 'public' >> .gitignore
echo 'resources' >> .gitignore
```

テーマ設定

```shell
git submodule add https://github.com/kakawait/hugo-tranquilpeak-theme.git themes/tranquilpeak
```

サイト設定

```shell
cp -pr themes/tranquilpeak/exampleSite/config.toml .
```

config.toml

```toml
baseURL = "http://heartfulmoon.github.io/"
languageCode = "ja"
title = "Heartfullmoon Web Site"
theme = "tranquilpeak"
```

> github pagesやnetlifyで使う場合はbaseURLのプロトコルはhttpsにすること


起動確認(http://localhost:1313)

```shell
cp /path/to/someplace/Makefile .
make run
```

Githubレポジトリ作成後

```shell
git remote add origin git@github.com:heartfulmoon/hearfulmoon.github.io.git
git add .
git commit -m 'init'
git push -u origin master
```

* Github>Settings>Gighub Pages>Source>gh-pages branchに設定する
* しばらく時間がかかる

## 既存のレポジトリからクローンする場合

```shell
git clone git@github.com:heartfulmoon/hearfulmoon.github.io.git hearfulmoon.github.io
cd hearfulmoon.github.io
git submodule update --init --recursive
```

## デプロイ設定

### Github Pages(Github Actionsの利用)

* .github/workflows/src-master.yamlを作成
* ソースはsrcブランチ
* 出力はpublicフォルダの内容をmasterブランチ
* Settings>Secretsに以下を追加
    * Name: HOST
    * Value: https://heartfulmooon.github.io/
* buildのコマンドに --baseUrl=${{ secrets.HOST }}を追加

### Netlify

* Site Settings>Build&deploy>Build settings
    * Repository: github.com/heartfulmoon/heartfulmoon.github.io
    * Build command: hugo --gc -minify --baseUrl="${HOST}"
    * Environment
        * Key: HOST
        * Value: https://heartfulmooon.netlify.app/

```shell
make deploy
```

## 使い方

### 投稿

新規投稿

```shell
hugo new ja/post/2020/05/helloworld.md
content/post/2020/05/helloworld created
```

文書作成

```shell
vi content/post/2020/05/helloworld
```

固定ページの作成

```shell
mkdir -p content/page/about/
i content/page/about/index.md
```

上記ファイル構成を元にconfig.tomlのメニューを設定

```toml
[[menu.main]]
  name = "Blog"
  url = "post"
  weight = 1

[[menu.main]]
  name = "Tags"
  url = "tags"
  weight = 2

[[menu.main]]
  name = "About"
  url = "page/about/"
  weight = 3
```

公開(githubにプッシュ)

```shell
make deploy
```

## Link

* [hugo\-tranquilpeak\-theme/user\.md at master · kakawait/hugo\-tranquilpeak\-theme](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/docs/user.md)
* [Hugo \+ Github Pagesでブログを公開してみた \- Qiita](https://qiita.com/eichann/items/4fe61b8b9bbafcfbe847)
* [GitHub PagesとHugoでブログをつくった \- meow\.md](https://uzimihsr.github.io/post/2019-08-07-create-blog-1/)
* [Hugoの導入から使い方とNetlifyでリリースするまでの方法](https://blog.cotapon.org/how-to-release-netlify-using-hugo/)
* [\[GitHub\]Actions Workflowへのtimeout指定のススメ \| Developers\.IO](https://dev.classmethod.jp/articles/must-set-timeout-on-actions-for-save-cost/)
