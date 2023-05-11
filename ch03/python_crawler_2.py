# 一覧ページからURLの一覧を抜き出す (2)

from typing import Iterator
import requests
import lxml.html


def main():
    """
    クローラーのメイン処理
    """
    response = requests.get('https://gihyo.jp/dp')
    # scrape_list_page()関数を呼び出し、ジェネレーターイテレーターを取得する。
    urls = scrape_list_page(response)
    # ジェネレーターイテレーターは、listなどと同様に繰り返し可能。
    for url in urls:
        print(url)


def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """
    一覧ページのResponseから詳細ページのURLを抜き出すジェネレーター関数
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        # yield文でジェネレーターイテレーターの要素を返す。
        yield url


if __name__ == '__main__':
    main()
