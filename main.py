import urllib.request


def get_request():
    # Cloud RunでデプロイしたエンドポイントURLに置き換えてください
    url = "https://your-cloud-run-url.a.run.app"  

    try:
        # URLにアクセスしてレスポンスを取得
        response = urllib.request.urlopen(url)
        
        # ステータスコードを確認
        status_code = response.getcode()
        if status_code == 200:
            print("URLリクエスト成功:", status_code)
        else:
            print("URLリクエスト失敗:", status_code)

    except urllib.error.URLError as e:
        print("URLエラー:", e.reason)
    except Exception as e:
        print("エラー:", e)

if __name__ == "__main__":
    get_request()
