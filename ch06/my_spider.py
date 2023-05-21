# Scrapinghub社のブログから投稿のタイトルを取得するSpider

import scrapy


class BlogSpider(scrapy.Spider):
    # Spiderの名前
    name = 'blogspider'
    # クロールを開始するURLのリスト
    # start_urls = ['https://blog.scrapinghub.com']
    start_urls = ['https://www.zyte.com/blog/']


    def parse(self, response):
        """
        ページから投稿のタイトルをすべて抜き出して、次のページへのリンクがあればたどる。
        """
        # ページから投稿のタイトルをすべて抜き出す
        # for title in response.css('.post-header>h2'):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        # 次のページ（OLDER POST）へのリンクがあればたどる
        # for next_page in response.css('a.next_posts-link'):
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
