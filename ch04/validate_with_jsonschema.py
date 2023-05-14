# jsonschemaによるバリデーション

from jsonschema import validate

# 4つのルールを持つスキーマ（期待するデータ構造）を定義する。
schema = {
    # ルール1: 値はJSONにおけるオブジェクト（Pythonにおけるdict）である。
    "type": "object",
    "properties": {
        # ルール2: nameの値は文字列である。
        "name": {
            "type": "string"
        },
        # ルール3: priceの値は文字列で、patternに指定した正規表現にマッチする。
        "price": {
            "type": "string",
            "pattern": "^[0-9,]+$"
        }
    },
    # ルール4: dictのキーとして、nameとpriceは必須である。
    "required": ["name", "price"]
}

# validate()関数は、第1引数のオブジェクトを第2引数のスキーマでバリデーションする。
#   スキーマに適合するので、例外は発生しない。
validate({
    'name': 'ぶどう',
    'price': '3,000',
}, schema)
#   スキーマに適合しないので、jsonschema.exceptions.ValidationError（例外）が発生する。
validate({
    'name': 'みかん',
    'price': '無料',
}, schema)
