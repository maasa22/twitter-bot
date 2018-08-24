#coding: utf-8
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time
import requests
import json
import twitter
#import myconf
import os

auth = twitter.OAuth(
        consumer_key = os.environ["consumer_key"],
        consumer_secret = os.environ["consumer_secret"],
        token = os.environ["token"],
        token_secret = os.environ["token_secret"],
        )
t = twitter.Twitter(auth=auth)

weather_apikey = os.environ["weather_apikey"]
cities = ["Tokyo,JP"]
weather_api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
k2c = lambda k: k - 273.15 #温度変換

print("天気速報")
for name in cities:
  url = weather_api.format(city=name, key=weather_apikey)
  r = requests.get(url)
  data = json.loads(r.text)
  print(data, '\n')
  d = datetime.today()
  print(d.strftime("%Y-%m-%d %H:%M:%S"))
  print("+ 都市=", data["name"])
  print("| 天気=", data["weather"][0]["description"])
  print("| 最低気温=", k2c(data["main"]["temp_min"]))
  print("| 最高気温=", k2c(data["main"]["temp_max"]))
  print("| 気温=", (format(k2c(data["main"]["temp"]), '.1f')) )
  print("| 湿度=", data["main"]["humidity"])
  print("| 気圧=", data["main"]["pressure"])
  print("| 風向き=", data["wind"]["deg"], " (north:0, east:90, south:180, west:270)")
  print("| 風速度=", data["wind"]["speed"])
  print("")

  present_time =d.strftime("%Y-%m-%d %H:%M:%S")

  status = present_time + '\n' + "都市= " + str(data["name"]) + '\n' \
        +"天気= "+str(data["weather"][0]["description"]) + '\n' \
        +"気温= "+ str(format(k2c(data["main"]["temp"]), '.1f')) + "℃" +'\n' \
        +"湿度= "+ str(data["main"]["humidity"]) +'\n' \
        +"気圧= "+ str(data["main"]["pressure"]) +'\n' \
        +"風向き= "+ str(data["wind"]["deg"])+ '\n' \
        +"風速度= "+ str(data["wind"]["speed"]) + '\n' \
        +"最低気温= "+ str(k2c(data["main"]["temp_min"])) + "℃" +'\n' \
        +"最高気温= "+ str(k2c(data["main"]["temp_max"])) + "℃" +'\n' \

  t.statuses.update(status=status)


#http://qiita.com/yuki_bg/items/96a1608aa3f3225386b6
