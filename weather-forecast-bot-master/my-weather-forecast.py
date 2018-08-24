#coding: utf-8
#天気速報Bot
#ファイル書き込みもしたい
#iOSアプリにしたい
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time
import requests
import json
import twitter
import emoji
import sys
import os
#import myconf #aaa


auth = twitter.OAuth(
        consumer_key = os.environ["consumer_key"],
        consumer_secret = os.environ["consumer_secret"],
        token = os.environ["token"],
        token_secret = os.environ["token_secret"],
        )

'''
auth = twitter.OAuth(
        consumer_key        = myconf.consumer_key,
        consumer_secret     = myconf.consumer_secret,
        token    = myconf.token,
        token_secret = myconf.token_secret,
        )
'''
t = twitter.Twitter(auth=auth)

#weather_apikey = myconf.weather_apikey
weather_apikey = os.environ["weather_apikey"]
cities = ["Tokyo,JP"]
weather_api = "http://api.openweathermap.org/data/2.5/forecast?units=metric&q={city}&APPID={key}"

def emoji_weather(weather_main):
  if weather_main == "Clear":
      return emoji.emojize(':sun:', use_aliases=True)
  elif weather_main == "Clouds":
      return emoji.emojize(':cloud:', use_aliases=True)
  elif weather_main == "Rain":
      return emoji.emojize(':umbrella:', use_aliases=True)
  else:
      return emoji.emojize(':question:', use_aliases=True)

fo = open('test.txt', 'w')
sys.stdout = fo

print("#forecast")
for name in cities:
  url = weather_api.format(city=name, key=weather_apikey)
  r = requests.get(url)
  data = json.loads(r.text)
  #print(data, '\n')
  #print(data["list"][0])
  #print(len(data["list"]))
  now_time = data["list"][0]["dt_txt"]
  #print("forecast time= ",now_time)
  #print(now_time[11:13]) #時の予報
  d = datetime.today()
  print(d.strftime("%Y-%m-%d %H:%M:%S"))


  #print("気温")
  print(data["list"][0]["dt_txt"][5:7]+"/"+data["list"][0]["dt_txt"][8:10])
  #print(data["list"][0]["dt_txt"][11:13]+"時 "+format(data["list"][0]["main"]["temp"], '.1f')+"℃",end="")
  #weather_main = data["list"][0]["weather"][0]["main"]
  #print(emoji_weather(weather_main))
  for i in range(3,12):
      weather_main = data["list"][i]["weather"][0]["main"]
      print(data["list"][i]["dt_txt"][11:13]+"時", format(data["list"][i]["main"]["temp"],'.1f'),end="")
      print(emoji_weather(weather_main))
  fo.close()
  fo2 = open("test.txt","r")
  allLines = fo2.read()
  fo2.close()
  status = allLines
  t.statuses.update(status=status)

  time.sleep(3.0)
  fo3 = open('test.txt', 'w')
  sys.stdout = fo3
  #print("空模様")
  print(d.strftime("%Y-%m-%d %H:%M:%S"))
  print(data["list"][0]["weather"][0]["description"], data["list"][3]["dt_txt"][5:13]+"時")
  for i in range(4,8):
      print(data["list"][i]["weather"][0]["description"], data["list"][i]["dt_txt"][10:13]+"時")
  fo3.close()
  fo4 = open("test.txt","r")
  allLines2 = fo4.read()
  fo4.close()
  status2 = allLines2
  t.statuses.update(status=status2)

  time.sleep(3.0)
  fo5 = open('test.txt', 'w')
  sys.stdout = fo5
  print(d.strftime("%Y-%m-%d %H:%M:%S"))
  print(data["list"][5]["weather"][0]["description"], data["list"][8]["dt_txt"][5:13]+"時")
  for i in range(9,13):
      print(data["list"][i]["weather"][0]["description"], data["list"][i]["dt_txt"][10:13]+"時")
  fo5.close()
  fo6 = open("test.txt","r")
  allLines3 = fo6.read()
  fo6.close()
  status3 = allLines3
  t.statuses.update(status=status3)


'''
#画像付きツイート
pic="test.png" #画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
 image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id_img1]))
'''
