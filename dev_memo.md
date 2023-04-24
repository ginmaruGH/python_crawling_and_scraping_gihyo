# 開発メモ

## Git

```bash
# リモートリポジトリのコピーを作成
git clone <repository-name>
```

---

## Python

- バージョン管理ツール
  - [asdf](https://asdf-vm.com/)

```bash
# Pythonのバージョン確認
python --version
```

```bash
# PCにインストールされているPythonのバージョンの確認
asdf list python
```

```bash
# カレントディレクトリのPythonのバージョンを指定する
asdf local python <version>
```

```bash
# パッケージのバージョンに合わせたシムの再作成
# https://asdf-vm.com/manage/commands.html
# https://zenn.dev/kyohei_saito/articles/40a13800f34d5f
asdf reshim
```

---

## 仮想環境の構築

```bash
# 仮想環境の構築
# python3 -m venv <env-name>
python3 -m venv venv
```

```bash
# 仮想環境への切り替え
source venv/bin/activate
```

```bash
# pipのアップグレード
pip install --upgrade pip
```

```bash
# 仮想環境にインストールされているパッケージの一覧作成
pip freeze > requirements.txt
```

```bash
# requirements.txtからパッケージをインストール
pip install -r requirements.txt
```

```bash
# requirements.txtからすべてのパッケージをアップグレード
pip install --upgrade -r requirements.txt
```

```bash
# 仮想環境の終了
deactivate
```

---

## Python Library Related

- [PyCaret Official](https://pycaret.gitbook.io/docs/)
  - `pip install pycaret[full]`
  - `pip install git+https://github.com/pycaret/pycaret.git#egg=pycaret`
- [Dash Python User Guide](https://dash.plotly.com/)
- [Plotly.py](https://plotly.com/python/)
- [SergeyPirogov/webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager)


## 正規表現

- [正規表現 メタ文字一覧](https://www.megasoft.co.jp/mifes/seiki/meta.html)
- [正規表現の記事](https://www-creators.com/archives/category/regexp)
  - [正規表現：否定先読み、肯定先読みについて](https://www-creators.com/archives/2746)
- [[Python] re.compile内で変数を使用する](https://tech.kx2.site/2021/08/24/python-re-compile%E5%86%85%E3%81%A7%E5%A4%89%E6%95%B0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B/)
- [Pythonで文字列を抽出（位置・文字数、正規表現）](https://note.nkmk.me/python-str-extract/)

## Scraping

- [Python BeautifulSoupの使い方を徹底解説！(select、find、find_all、インストール、スクレイピングなど)](https://ai-inter1.com/beautifulsoup_1/#st-toc-h-14)
- [pandasのread_htmlがデータを読み込めない](https://teratail.com/questions/e069selc4rg5tn)
- [urllib.requestモジュールによるWebページの取得](https://atmarkit.itmedia.co.jp/ait/articles/1910/15/news018.html)
  - charset について
- [Beautiful Soup のfind_all( ) と select( ) の使い方の違い](https://gammasoft.jp/blog/difference-find-and-select-in-beautiful-soup-of-python/)
- [WebスクレイピングのためのCSSセレクタの基本](https://gammasoft.jp/support/css-selector-for-python-web-scraping/)
- [Python, Requestsの使い方](https://note.nkmk.me/python-requests-usage/)
- [Upgrade to Selenium 4](https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/#executable_path-has-been-deprecated-please-pass-in-a-service-object)
- [SergeyPirogov/webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager)
- [スクレイピング時にChromeDriverを自動更新するライブラリが便利](https://next-k.site/blog/archives/2021/11/18/628)

## JSON

- [datetimeやsetのJSON化](https://www.python.ambitious-engineer.com/archives/3805)

## datetime

- [Create Year-Month Column from Dates](https://dfrieds.com/data-analysis/create-year-month-column.html)

## Database

- SQLite
  - [SQLite データベースに対する DB-API 2.0](https://docs.python.org/ja/3/library/sqlite3.html)
  - [sqlitebrowser/sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser)
  - [Pythonで簡単にデータベースを扱う(SQLite3)](https://qiita.com/ku_a_i/items/9c68e8aed3c2c066bc60)
  - [Pythonで簡単にデータベースを扱う(SQLite3) その２](https://qiita.com/ku_a_i/items/ddd9408ed287326721f9)
  - [SQLite3入門](https://www.python.ambitious-engineer.com/archives/745)
- SQLAlchemy
  - [SQLAlchemy入門 SQLAlchemyとは](https://www.python.ambitious-engineer.com/archives/1469)
  - [SQLAlchemy 概要と基本の使い方](https://zenn.dev/myuki/books/02fe236c7bc377)
- JRA-VAN
  - [JRA-VAN SDK](http://jra-van.jp/dlb/sdv/sdk.html)
    - [Mac から Windows へリモートデスクトップ接続 - アプリ「Microsoft Remote Desktop」](https://pc-karuma.net/mac-app-microsoft-remote-desktop-10/)
    - [リモートデスクトップ接続できない場合の対処方法](https://pc-karuma.net/mcafee-windows-remote-desktop/)
    - [リモートデスクトップ](https://pc-karuma.net/tag/remote-desktop/)

## Logging

- [Logging HOWTO 基本 logging チュートリアル](https://docs.python.org/ja/3/howto/logging.html#logging-basic-tutorial)
- [Logging HOWTO 上級 logging チュートリアル](https://docs.python.org/ja/3/howto/logging.html#logging-advanced-tutorial)
- [Logging クックブック](https://docs.python.org/ja/3/howto/logging-cookbook.html#logging-cookbook)
- [logging モジュールの API リファレンス](https://docs.python.org/ja/3/howto/logging.html)
- [logging.config --- ロギングの環境設定](https://docs.python.org/ja/3/library/logging.config.html#logging-config-api)
- [logging.handlers --- ロギングハンドラ](https://docs.python.org/ja/3/library/logging.handlers.html#module-logging.handlers)
- [Pythonでprintを卒業してログ出力をいい感じにする](https://qiita.com/FukuharaYohei/items/92795107032c8c0bfd19)
- [【Python】仕組みを理解してログ出力を使いこなす](https://hackers-high.com/python/logging-overview/)
- [logging 基本的な使い方](https://www.python.ambitious-engineer.com/archives/693)

## References

- [【解説】データサイエンス100本ノックの始め方](https://omathin.com/100knocks-getstart/)

## Community

[comp.lang.python](https://groups.google.com/g/comp.lang.python)

## VS Code

- [拡張機能を無効化しても重いVS Codeを軽かった頃に戻す方法](https://qiita.com/tatsubey/items/e14e214c81057b22d82a)
- [VSCodeで、ファイルを開くのにやたらと時間がかかって遅いのを改善する(VSCodeの起動の遅さではない)](https://dekuo-03.hatenablog.jp/entry/2022/07/24/111937)
- [Visual Studio Codeの起動が遅いときに試すこと](https://zenn.dev/korinvr/articles/vscode-performance)

## Pandas

- [【Pandas】両者のDataframeの差分を確認したい！](https://qiita.com/higakin/items/59b60ed10ea0c0348362)
