import MySQLdb

# MySQLサーバーに接続して、コネクションを取得する。
# ユーザー名とパスワードを指定して、scrapingデータベースを使用する。
# 接続に使用する文字コードは、utf8mb4とする。
conn = MySQLdb.connect(
    db='scraping',
    user='scraper',
    password='password',
    charset='utf8mb4'
)

# カーソルを取得する。
c = conn.cursor()
# execute()メソッドでSQL文を実行する。
# このスクリプトを何回実行しても同じ結果になるようにするため、citiesテーブルが存在する場合は削除する。
c.execute('DROP TABLE IF EXISTS `cities`')
# citiesテーブルを作成する。
c.execute("""
    CREATE TABLE `cities` (
        `rank` integer,
        `city` text,
        `population` integer
    )
""")

# execute()メソッドの第2引数には、SQL文のパラメータを指定できる。
# パラメータで置き換える場所（プレースホルダー）は、%sで指定する。
c.execute('INSERT INTO `cities` VALUES (%s, %s, %s)', (1, '上海', 24150000))

# パラメータが辞書の場合、プレースホルダーは %(名前)s で指定する。
c.execute(
    'INSERT INTO `cities` VALUES (%(rank)s, %(city)s, %(population)s)',
    {'rank': 2, 'city': 'カラチ', 'population': 23500000}
)

# executemany()メソッドでは、複数のパラメーターをリストで指定できる。
# パラメータの数（ここでは3つ）のSQLを実行できる。
c.executemany(
    'INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
    [
        {'rank': 3, 'city': '北京', 'population': 21516000},
        {'rank': 4, 'city': '天津', 'population': 14722100},
        {'rank': 5, 'city': 'イスタンブル', 'population': 14160467},
    ]
)

# 変更をコミットする。
conn.commit()

# 保存したデータを取得する。
c.execute('SELECT * FROM `cities`')

# クエリの結果は、fetchall()メソッドで取得できる。
for row in c.fetchall():
    # 取得したデータを表示する。
    print(row)

# コネクションを閉じる。
conn.close()
