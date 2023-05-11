# 詳細ページからスクレイピング

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
        # sessionを使って詳細ページを取得する。
        response = session.get(url)
        # 詳細ページからスクレイピングして電子書籍の情報を取得する。
        ebook = scrape_detail_page(response)
        # 電子書籍の情報を表示する。
        print(ebook)
        # 1ページだけ試すため、break文でループを抜ける。
        break


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
        # .textで直接の子要素である文字列のみを取得する
        'price': html.cssselect('.buy')[0].text,
        # 目次
        'content': [h3.text_content() for h3 in html.cssselect('#content > h3')]
    }
    return ebook


if __name__ == '__main__':
    main()
