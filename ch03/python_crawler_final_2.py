# 最終的なクローラー
# - 取得したデータをMongoDBに保存する。
# - キーを設計する。
# - 2回目以降のクロール済みのURLはクロールしない。

import re
import time
from typing import Iterator
import requests
import lxml.html
from pymongo import MongoClient
import pymongo


def main():
    """
    クローラーのメインの処理
    """
    # ローカルホストのMongoDBに接続する。
    client = MongoClient('mongodb://localhost:27017/')
    # scrapingデータベースのebooksコレクションを取得する。
    collection = client.scraping.ebooks
    # データを一意に識別するキーを格納するkeyフィールドにユニークなインデックスを作成する。
    collection.create_index('key', unique=True)

    # 複数のページをクロールするので、Session()を使う。
    session = requests.Session()
    # 一覧ページを取得する。
    response = requests.get('https://gihyo.jp/dp')
    # 詳細ページのURL一覧を取得する。
    urls = scrape_list_page(response)
    for url in urls:
        # URLからキーを取得する。
        key = extract_key(url)

        # MongoDBからkeyに該当するデータを探す。
        ebook = collection.find_one({'key': key})
        # MongoDBに存在しない場合のみ、詳細ページをクロールする。
        if not ebook:
            # 1秒のウェイトを入れる。
            time.sleep(1)
            # sessionを使って詳細ページを取得する。
            response = session.get(url)
            # 詳細ページからスクレイピングして電子書籍の情報を取得する。
            ebook = scrape_detail_page(response)
            # 電子書籍の情報をMongoDBに保存する。
            # collection.insert_one(ebook)
            try:
                collection.insert_one(ebook)
            except pymongo.errors.DuplicateKeyError:
                # Handle the case where a document with the same key already exists
                # 同じkeyを持つドキュメントが既に存在する場合の処理
                pass

        # 電子書籍の情報を表示する。
        print(ebook)


def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """
    一覧ページのResponseから詳細ページのURLを抜き出すジェネレーター関数
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        yield url


def scrape_detail_page(response: requests.Response) -> dict:
    """
    詳細ページのResponseから電子発赤の情報をdictで取得する。
    """
    html = lxml.html.fromstring(response.text)
    ebook = {
        # URL
        'url': response.url,
        # タイトル
        'title': html.cssselect('#bookTitle')[0].text_content(),
        # 価格
        # .textで直接の子要素である文字列のみを取得する。
        # strip()で前後の空白を削除する。
        'price': html.cssselect('.buy')[0].text.strip(),
        # 目次
        'content': [
            normalize_spaces(h3.text_content()) for h3 in html.cssselect('#content > h3')
        ],
    }
    # dictを返す。
    return ebook


def extract_key(url: str) -> str:
    """
    URLからキー（URLの末尾のISBN）を抜き出す
    """
    # 最後の`/`から文字列末尾までを正規表現で取得する。
    m = re.search(r'/([^/]+)$', url)
    if m:
        return m.group(1)
    else:
        # handle the case where the regular expression did not match
        return ''


def normalize_spaces(s: str) -> str:
    """
    連続する空白を1つのスペースに置き換え、
    前後の空白を削除した新しい文字列を取得する
    """
    # re.sub(正規表現パターン, 置換先文字列, 処理対象)
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()
