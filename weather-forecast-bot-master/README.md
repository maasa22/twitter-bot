# twitter-bot
自分用備忘録

herokuで実行しているのは、my-weather-report.py。

これを、heroku schedulerで定期実行している。

さらに、my-weather-forecast.py。１日１回。

環境変数をherokuに設定しており、そこから読み込んでいる。

Procfile: webとworkerで上手くいったり、いかなかったり。

index.py: ダミーの実行ファイル（必要ならしい。）

requirements.txt: 必要なモジュールのインポート

runtime.txt: pythonのversionを指定

この4つは、多分必要らしい。
