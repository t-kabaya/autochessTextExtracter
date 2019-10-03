pip3 install
pip3 freeze > requirements.txt
を忘れないようにしてください。

## テスト
python 標準のunittestで、単体テストのみ行う。

## インフラ
google app engineを使用。
依存関係はシンプルにrequirements.txtで管理する。

## 使用ライブラリ
Flask
マイクロサーバーを建てるのに使用。
getリクエストさえ出来れば良いため、あまりに詳しく調べず、雑に使っている。
調査すれば、もっと良い書き方が出来そう。

cloud vision api
画像から、文字列を抽出するのに使用。

## 概要
画像のurlを受け取り、画像中のtextを抽出するapi