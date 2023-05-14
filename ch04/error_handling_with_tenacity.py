# ライブラリーtenacityを使って、リトライ処理を簡潔に書く

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

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


# @retryデコレーターのキーワード引数
#   stopにリトライを終了する条件を指定する。
#   waitにウェイトの取り方を指定する。
# stop_after_attemptは回数を条件に終了することを表す。
#   引数に最大リトライ回数を指定する。
# wait_exponentialは指数関数的なウェイトを表す。
#   キーワード引数multiplierに初回のウェイトを秒単位で指定する。
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
def fetch(url: str) -> requests.Response:
    """
    指定したURLにリクエストを送り、Responseオブジェクトを返す。
    一時的なエラーが起きた場合、最大3回リトライする。
    3回リトライしても成功しなかった場合、tenacity.RetryError（例外）を発生させる。
    """
    print(f'Retrieving {url}...')
    response = requests.get(url)
    print(f'Status: {response.status_code}')

    if response.status_code not in TEMPORARY_ERROR_CODES:
        # 一時的なエラーでなければ、responseを返して終了する。
        return response

    # 一時的なエラーの場合、例外を発生させてリトライする。
    raise Exception(f'Temporary Error: {response.status_code}')


if __name__ == '__main__':
    main()
