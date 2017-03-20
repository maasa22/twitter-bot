#coding: utf-8
#今の天気をtwitterで呟く、Herokuにやらせる方が良いかも
#ファイル書き込みもしたい

from crontab import CronTab
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time
import requests
import json
import twitter
import myconf

auth = twitter.OAuth(
        consumer_key        = myconf.consumer_key,
        consumer_secret     = myconf.consumer_secret,
        token    = myconf.token,
        token_secret = myconf.token_secret,
        )
t = twitter.Twitter(auth=auth)

weather_apikey = myconf.weather_apikey
cities = ["Tokyo,JP"]
weather_api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
k2c = lambda k: k - 273.15 #温度変換

class JobConfig(object):
  def __init__(self, crontab, job):
    self._crontab = crontab
    self.job = job

  def schedule(self):
    crontab = self._crontab
    return datetime.now() + timedelta(seconds=math.ceil(crontab.next()))

  def next(self):
    crontab = self._crontab
    return math.ceil(crontab.next())

def job_controller(jobConfig):
  logging.info("->- 処理を開始しました。")
  while True:
    try:
      logging.info("-?- 次回実行日時\tschedule:%s" %
        jobConfig.schedule().strftime("%Y-%m-%d %H:%M:%S"))
      time.sleep(jobConfig.next())
      jobConfig.job()
    except KeyboardInterrupt:
      break
  logging.info("-<- 処理を終了しました。")

def job1():
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
      print("| 気温=", k2c(data["main"]["temp"]))
      print("| 湿度=", data["main"]["humidity"])
      print("| 気圧=", data["main"]["pressure"])
      #print("| 風向き=", data["wind"]["deg"], " (north:0, east:90, south:180, west:270)")
      print("| 風速度=", data["wind"]["speed"])
      print("")
      #ツイートのみ
      #temp = format(k2c(data["main"]["temp"]),'.1f')
      #status = "tokyo : " + str(temp) + "℃"  #投稿するツイート
      present_time =d.strftime("%Y-%m-%d %H:%M:%S")
      #今の時刻を呟かせるようにすると、重複しない
      status = present_time + '\n' + "気温= " + str(format(k2c(data["main"]["temp"]), '.1f'))
      t.statuses.update(status=status)


def job2():
  logging.debug("処理2")


def main():
  '''
  logging.basicConfig(level=logging.DEBUG,
    format="time:%(asctime)s.%(msecs)03d\tprocess:%(process)d" +
      "\tmessage:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
  '''
  print("お天気速報")
  jobConfigs = [
    JobConfig(CronTab("* * * * *"), job1),
    #JobConfig(CronTab("*/2 * * * *"), job2)
  ]
  p = Pool(len(jobConfigs))
  try:
    p.map(job_controller, jobConfigs)
  except KeyboardInterrupt:
    pass

if __name__ == "__main__":
  main()

'''
#画像付きツイート
pic="test.png" #画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
 image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id_img1]))
'''

#http://qiita.com/yuki_bg/items/96a1608aa3f3225386b6
