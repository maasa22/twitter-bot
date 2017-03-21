# twitter-bot
自分用備忘録
herokuで実行しているのは、twitter-bot-no-repeat.py。これを、heroku schedulerで定期実行している。
環境変数をherokuに設定しており、そこから読み込んでいる。

Procfile: 
index.py: ダミーの実行ファイル（必要ならしい。）
requirements.txt: 必要なモジュールのインポート
runtime.txt: pythonのversionを指定
この4つは、多分必要らしい。

localで実行する時は、twitter-bot-local.py。gitには上げていないが、必要な変数は
myconfに定義している。

twitter-bot.pyは、cronとherokuの相性が悪いのか、上手くいかなかった。503error。
