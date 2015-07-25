# -- coding:utf-8 --
__author__ = 'chenziheziye'


f = open('/Users/chenziheziye/Documents/history_data.txt', 'r')

try:
    num1 = input("\n请输入第1个(红球)号码：")
    num2 = input("\n请输入第2个(红球)号码：")
    num3 = input("\n请输入第3个(红球)号码：")
    num4 = input("\n请输入第4个(红球)号码：")
    num5 = input("\n请输入第5个(红球)号码：")
    num6 = input("\n请输入第6个(红球)号码：")
    num7 = input("\n请输入(蓝球)号码：")
except:
    print("\n输入非法，请输入01,02...33, 01,02...16")

numList = "{0:02d}".format(num1),"{0:02d}".format(num2),"{0:02d}".format(num3), \
          "{0:02d}".format(num4),"{0:02d}".format(num5),"{0:02d}".format(num6), \
          "{0:02d}".format(num7)
blueNum = 0

print "选中的号码集合为:", numList

for line in f:
    curList = line.split()
    hitNum = 0

    for num in numList[0:6]:
        if num in curList[1:7]:
            hitNum += 1

    if hitNum >= 6:
        print "\n出现命中号码：", curList
        break

print "温馨提示：恭喜您！所选号码与历史中大奖的号码未发生重合！"

f.close()