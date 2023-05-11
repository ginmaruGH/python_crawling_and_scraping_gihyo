# 一覧ページからURLの一覧を抜き出す (1)

import requests
import lxml.html

response = requests.get('https://gihyo.jp/dp')
html = lxml.html.fromstring(response.text)
# 絶対URLに変換する。
html.make_links_absolute(response.url)

for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    url = a.get('href')
    print(url)
