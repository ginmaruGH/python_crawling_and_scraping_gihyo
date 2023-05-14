# CacheControlを使ってキャッシュを処理する。

import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache


session = requests.Session()
# sessionをラップしたcached_sessionを作る。
# キャッシュはファイルとして、`.webcache`ディレクトリ内に保存する。
cached_session = CacheControl(session, cache=FileCache('.webcache'))

# 通常のSessionと同様に使用する。
response = cached_session.get('https://docs.python.org/3/')

# response.from_cache属性でキャッシュから取得されたレスポンスかどうかを取得できる。
# 初回は、`False`。2回目以降は、`True`。
print(f'from_cache: {response.from_cache}')
# ステータスコードを表示する。
print(f'status_code: {response.status_code}')
# レスポンスボディを表示する。
print(response.text)
