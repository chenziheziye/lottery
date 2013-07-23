import urllib
from lxml import html

dataFile = open('/Users/chenziheziye/Documents/history_data.txt', 'a+')


pageNum = 1

while pageNum < 51:

    URL_2003_2013 = 'http://baidu.lecai.com/lottery/draw/list/50?lottery_type=50&page=%d&ds=2003-01-18&de=2013-07-18'%(pageNum)
    page = html.fromstring(urllib.urlopen(URL_2003_2013).read())

    for elem in page.xpath("//span[@class='result']"):
        date = elem[0].xpath("../../preceding-sibling::td[@class='td1']")
        data = [date[0].text+' ',elem[0].text+' ',elem[1].text+' ',elem[2].text+' ',elem[3].text+' ',
                elem[4].text+' ',elem[5].text+' ',elem[6].text+'\n']
        dataFile.writelines(data)

    pageNum += 1






#html -- body -- div class='main' -- div class='right_main' -- 4th div -- tbody(30)
#tbody -- tr -- td class='td1' date, td class='td3'--span--span class='ball_1' red, class='ball_2' blue
