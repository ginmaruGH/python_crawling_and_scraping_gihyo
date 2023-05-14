# HTTPステータスコードに応じたエラー処理

import time

import requests

# 408: Request Timeout（一定時間内にリクエストが完了しなかった。）
# 500: Internal Server Error（サーバー内部で予期せぬエラーが発生した。）
# 502: Bad Gateway（ゲートウェイサーバが背後のサーバーからエラーを受け取った。）
# 503: Service Unavailable（サーバーは一時的にリクエストを処理できない。）
# 504: Gateway Timeout（ゲートウェイサーバーから背後のサーバーへのリクエストがタイム・アウトした。）
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)


def main():
    """
    メインとなる処理。
    """
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error!')


def fetch(url: str) -> requests.Response:
    """
    指定したURLにリクエストを送り、Responseオブジェクトを返す。
    一時的なエラーが起きた場合、最大3回リトライする。
    3回リトライしても成功しなかった場合、Exception（例外）を発生させる。
    """
    # 最大3回リトライする。
    max_retries = 3
    # 現在のリトライ回数
    retries = 0
    while True:
        try:
            print(f'Retrieving {url}...')
            response = requests.get(url)
            print(f'Status: {response.status_code}')
            if response.status_code not in TEMPORARY_ERROR_CODES:
                # 一時的なエラーでなければ、responseを返して終了する。
                return response
        except requests.exceptions.RequestException as ex:
            # ネットワークレベルのエラー（RequestException）の場合、ログを出力してリトライする。
            print(f'Network-level exception occured: {ex}')

        # リトライ処理
        retries += 1
        if retries >= max_retries:
            # リトライ回数の上限を超えた場合、例外を発生させる。
            raise Exception('Too many retries.')

        # 指数関数的なリトライ間隔を求める。
        wait = 2**(retries - 1)
        print(f'Waiting {wait} seconds...')
        # ウェイトを取る。
        time.sleep(wait)


if __name__ == '__main__':
    main()
