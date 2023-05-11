# 詳細ページをクロールする（1）

import re
import time
from typing import Iterator
import requests
import lxml.html


def main():
    """
    クローラーのメインの処理
    """
    # 複数のページをクロールするので、Session()を使う。
    session = requests.Session()
    response = requests.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        # 1秒のウェイトを入れる。
        time.sleep(1)
        # sessionを使って詳細ページを取得する。
        response = session.get(url)
        # 詳細ページからスクレイピングして電子書籍の情報を取得する。
        ebook = scrape_detail_page(response)
        # 電子書籍の情報を表示する。
        print(ebook)
        # 1ページだけ試すため、break文でループを抜ける。
        # break


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
    return ebook


def normalize_spaces(s: str) -> str:
    """
    連続する空白を1つのスペースに置き換え、
    前後の空白を削除した新しい文字列を取得する
    """
    # re.sub(正規表現パターン, 置換先文字列, 処理対象)
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()
