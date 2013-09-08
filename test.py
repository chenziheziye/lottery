# -- coding:utf-8 --

import urllib
from lxml import html
import os
import time

data_file_path = '/Users/chenziheziye/Documents/history_data.txt'

if os.path.exists(data_file_path):
    os.remove(data_file_path)

dataFile = open(data_file_path, 'a+')

#返回字典
def GetCurTime():

    curTime = time.gmtime()
    strCurTime = str(curTime.tm_year) + '-' + '{0:02d}'.format(curTime.tm_mon) + '-' + '{0:02d}'.format(curTime.tm_mday)
    strLastTime = str(curTime.tm_year) + '-' + '{0:02d}'.format(curTime.tm_mon) + '-01'
    return {'curDay':strCurTime, 'lastDay':strLastTime, 'year':curTime.tm_year, 'mon':curTime.tm_mon}

#html -- body -- div class='main' -- div class='right_main' -- 4th div -- tbody(30)
#tbody -- tr -- td class='td1' date, td class='td3'--span--span class='ball_1' red, class='ball_2' blue
#http://baidu.lecai.com/lottery/draw/list/50?ds=2003-02-01&de=2003-03-01
def FetchLotteryDataAll():

    timeDic = GetCurTime()
    TIME_URL = 'http://baidu.lecai.com/lottery/draw/list/50?ds='

    #2003-02-01开始才有了双色球数据
    _year = 2003
    _mon = 02
    while True:

        if(_mon >= 12):
            _year += 1
            _mon = 1
        else:
            _mon += 1

        TIME_URL += str(_year) + '-' + '{0:02d}'.format(_mon-1) + '-01'#起始时间

        if(_year >= timeDic['year']) and (_mon >= timeDic['mon']):
            TIME_URL += '&de=' + timeDic['curDay']#终结时间
        else:
            TIME_URL += '&de=' + str(_year) + '-' + '{0:02d}'.format(_mon) + '-01'#终结时间

        page = html.fromstring(urllib.urlopen(TIME_URL).read())

        for elem in page.xpath("//span[@class='result']"):
            date = elem[0].xpath("../../preceding-sibling::td[@class='td1']")
            data = [date[0].text+' ',elem[0].text+' ',elem[1].text+' ',elem[2].text+' ',elem[3].text+' ',
                    elem[4].text+' ',elem[5].text+' ',elem[6].text+'\n']
            dataFile.writelines(data)

        if(_year >= timeDic['year']) and (_mon >= timeDic['mon']):
            break

FetchLotteryDataAll()

#dic = GetCurTime()
#print dic
