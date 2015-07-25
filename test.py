#!/usr/bin/env python2.7
# -- coding:utf-8 --
"""
module target:
   get lottery data from baidu.lecai.com and save data in file
dependency module:
   use urllib.urlopen(lind_addr).read() to get data
   use lxml.html.fromstring to filter data
method:
   GetCurTime - return a dict contain current year, month, day
   FetchLotteryDataAll - main process for getting, filtering, and saving data
"""
import urllib
from lxml import html
import os
import time

data_file_path = '/Users/chenziheziye/Documents/history_data.txt'

if os.path.exists(data_file_path):
    os.remove(data_file_path)

dataFile = open(data_file_path, 'a+')

#ret：eg.{'lastDay': '2013-10-01', 'mon': 10, 'curDay': '2013-10-25', 'year': 2013}
def GetCurTime():

    curTime = time.gmtime()
    strCurTime = str(curTime.tm_year) + '-' + '{0:02d}'.format(curTime.tm_mon) + '-' + '{0:02d}'.format(curTime.tm_mday)
    strLastTime = str(curTime.tm_year) + '-' + '{0:02d}'.format(curTime.tm_mon) + '-01'
    return {'curDay':strCurTime, 'lastDay':strLastTime, 'year':curTime.tm_year, 'mon':curTime.tm_mon}

#html -- body -- div class='main' -- div class='right_main' -- 4th div -- tbody(30)
#tbody -- tr -- td class='td1' date, td class='td3'--span--span class='ball_1' red, class='ball_2' blue
#http://baidu.lecai.com/lottery/draw/list/50?ds=2003-02-01&de=2003-03-01
#将网站获取的双色球数据按照：date r r r r r r b（per-line-format, r=red number, b=blue number）存到data_file_path
def FetchLotteryDataAll():

    timeDic = GetCurTime()

    #2003-02-01开始才有了双色球数据
    _year = 2003
    _mon = 02

    while True:

        if(_mon >= 12):
            _year += 1
            _mon = 02
        else:
            _mon += 1

        #起始时间
        TIME_URL = 'http://baidu.lecai.com/lottery/draw/list/50?ds=' + str(_year) + '-' + '{0:02d}'.format(_mon-1) + '-02'

        #终结时间
        if(_year >= timeDic['year']) and (_mon >= timeDic['mon']):
            TIME_URL += '&de=' + timeDic['curDay']
        else:
            TIME_URL += '&de=' + str(_year) + '-' + '{0:02d}'.format(_mon) + '-01'

        print TIME_URL
        page = html.fromstring(urllib.urlopen(TIME_URL).read())

        data = []
        for elem in page.xpath("//span[@class='result']"):
            date = elem[0].xpath("../../preceding-sibling::td[@class='td1']")
            data = [date[0].text+' ',elem[0].text+' ',elem[1].text+' ',elem[2].text+' ',elem[3].text+' ',
                    elem[4].text+' ',elem[5].text+' ',elem[6].text+'\n'] + data

        dataFile.writelines(data)

        if(_year >= timeDic['year']) and (_mon >= timeDic['mon']):
            break

def UpdateLotteryData():



FetchLotteryDataAll()

#测试代码
#dic = GetCurTime()
#print dic