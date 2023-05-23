# IKEA.comをクロールするSitemapSpider

from scrapy.spiders import SitemapSpider


class IkeaSpider(SitemapSpider):
    name = 'ikea'
    allowed_domains = ['www.ikea.com']

    # この設定がないと 504 Gateway Time-out となることがある。
    # settings.pyでUSER_AGENTを設定している場合、この設定は削除してよい。
    custom_settings = {
        'USER_AGENT': 'ikeabot',
    }

    # XMLサイトマップのURLのリスト。
    # robots.txtのURLを指定すると、SitemapディレクティブからXMLサイトマップのURLを取得する。
    sitemap_urls = [
        'https://www.ikea.com/robots.txt',
    ]

    # サイトマップインデックスからたどるサイトマップURLの正規表現のリスト。
    # このリストの正規表現にマッチするURLのサイトマップのみをたどる。
    # sitemap_followを指定しない場合、すべてのサイトマップをたどる。
    sitemap_follow = [
        # 日本語の製品のサイトマップのみたどる。
        r'prod-ja-JP',
    ]

    # サイトマップに含まれるURLを処理するコールバック関数を指定するルールのリスト。
    # ルールは、以下の2つの要素のタプルで指定する。
    # (<正規表現>, <正規表現にマッチするURLを処理するコールバック関数>)
    # sitemap_rulesを指定しない場合、すべてのURLのコールバック関数はparseメソッドとなる。
    sitemap_rules = [
        # 製品ページをparse_productで処理する。
        (r'/products/', 'parse_product'),
    ]


    def parse_product(self, response):
        """
        製品ページから製品の情報を抜き出す。
        """
        yield {
            # URL
            'url': response.url,
            # 名前
            'name': response.css('#name::text').get().strip(),
            # 種類
            'type': response.css('#type::text').get().strip(),
            # 価格
            # 円記号と数値の間に`\xa0`（HTMLでは、&nbsp;）が含まれるので、これをスペースに置き換える。
            'price': response.css('#price1::text').re_first('[\S\xa0]+').replace('\xa0', ''),
        }
