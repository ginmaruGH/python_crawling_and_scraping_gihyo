import scrapy

# ItemのHeadlineクラスをインポートする
from myproject.items import Headline


class NewsSpider(scrapy.Spider):
    """
    name属性
        Spiderの名前
    allowed_domains属性
        クロールを許可するドメインのリストを指定
    start_urls属性
        クロールを開始するURLのリストを指定
    """
    # Spiderの名前
    name = "news"
    # クロール対象とするドメインのリスト
    allowed_domains = ["news.yahoo.co.jp"]
    # クロールを開始するURLのリスト
    start_urls = ["https://news.yahoo.co.jp/"]


    def parse(self, response):
        """
        取得したWebページを処理するためのコールバック関数
        トップページのトピックス一覧から個々のトピックスへのリンクを抜き出してたどる。
        """
        # print(response.css('ul.topicsList_main a::attr("href")').getall())
        # print(response.css('li.sc-fHCHyC a::attr("href")').getall())

        for url in response.css('li.sc-fHCHyC a::attr("href")').re(r'/pickup/\d+$'):
            yield response.follow(url, self.parse_topics)


    def parse_topics(self, response):
        """
        トピックスのページからタイトルと本文を抜き出す。
        """
        # Headlineオブジェクトを作成する。
        item = Headline()
        # タイトル
        item['title'] = response.css('.sc-lbIafc::text').get()
        # 本文
        item['body'] = response.css('.highLightSearchTarget').xpath('string()').get()
        # Itemをyieldして、データを抽出する。
        yield item
