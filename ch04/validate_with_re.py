# 正規表現で価格として正しいかチェックする。

import re


def validate_price(value: str):
    """
    valueが価格として正しい文字列（数字とカンマを含む文字列）であるかどうかを判別する。
    正しくない場合、ValueError（例外）を発生させる。
    """
    # 数字とカンマのみを含む正規表現に、マッチするかチェックする。
    if not re.search(r'^[0-9,]+$', value):
        # マッチしない場合、例外を発生させる。
        raise ValueError(f'Invalid price: {value}')


# 価格として正しく文字列なので、例外は発生しない。
validate_price('3,000')
# 価格として正しくない文字列なので、例外が発生する。
validate_price('無料')
