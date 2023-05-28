# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class MyprojectPipeline:
#     def process_item(self, item, spider):
#         return item


from scrapy.exceptions import DropItem


class ValidationPipeline:
    """
    Itemを検証するPipeline。
    """


    def process_item(self, item, spider):
        if not item['title']:
            # titleフィールドが取得できない場合、破棄する。
            # DropItem()の引数は破棄する理由を表すメッセージ。
            raise DropItem('Missing title')

        # titleフィールドが正しく取得できている場合。
        return item
