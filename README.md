# twitter-bot
### 概要
1時間に1回東京の天気を、1日に1回東京の天気予報をつぶやくbot。
https://twitter.com/WeatherBot22

### プログラムの動き
herokuで実行しているのは、twitter-bot-no-repeat.py。  
これを、heroku schedulerで定期実行している。  
環境変数をherokuに設定しており、そこから読み込んでいる。   

### 必要らしい4つのファイル
Procfile:   
index.py: ダミーの実行ファイル（必要ならしい。）  
requirements.txt: 必要なモジュールのインポート  
runtime.txt: pythonのversionを指定  

### localで実行する時
localで実行する時は、twitter-bot-local.py。
gitには上げていないが、必要な変数はmyconfに定義している。   
twitter-bot.pyは、cronとherokuの相性が悪いのか、上手くいかなかった。503error。    
