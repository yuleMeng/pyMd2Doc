# -*- coding: utf-8 -*-
import re
import os
import json
pattern = '#+\s'

heading = {
        'heading1': 0,
        'heading2': -1,
        'heading3': -1,
        'heading4': -1,
        'heading5': -1,
        'heading6': -1
    }


def formatHeading():
    heading['heading1'] = 0
    heading['heading2'] = -1
    heading['heading3'] = -1
    heading['heading4'] = -1
    heading['heading5'] = -1
    heading['heading6'] = -1


def updateHeading(current, headId):
    for i in range(1, 6):
        if len(current) == i:
            heading['heading%r' % i] = headId


def getMenu():
    filename = os.getcwd()+'/title.md'
    titles = []
    global heading
    global newHeading
    headId = 1
    current = None
    preCurrent = '$'
    parentID = 0
    with open(filename, 'r', encoding='UTF-8') as f:
        for i in f.readlines():
            title = {}
            if not re.match(pattern, i.strip(' \t\n')):
                continue
            i = i.strip(' \t\n')
            current = i.split(' ')[0]
            # 当前标题级别比前一个小，则当前标题的父类标题是上一个的headId
            # 注释：#越多级别越小
            # 不论大多少个级别，只要父类级别大就是它的父类
            if len(current) > len(preCurrent):
                parentID = headId - 1
                # 更新当前级别父类
                updateHeading(current, parentID)
            # 当前级别比父类级别大，则去heading中寻找记录过的父类级别
            # 注释：#越少级别越大
            elif len(current) < len(preCurrent):
                length = len(current)
                # 当在文中出现一级标题的时候还原所有父类级别到初始值
                if length == 1:
                    formatHeading()
                    # 给当父类结果类赋值
                    parentID = 0
                else:
                    getVal = heading['heading%r' % length]
                    # 如果有记录过该级别的父类项
                    if getVal != -1:
                        parentID = getVal
                    # 改级别项没有记录则依次向上找父类，指导找到一级标题
                    else:
                        for j in range(length, 1, -1):
                            tempVal = heading['heading%r' % j]
                            if tempVal != -1:
                                parentID = tempVal
                                break
            titleName = i[len(current):].strip(' \t\n')
            title['titleName'] = titleName
            title['titleID'] = headId
            title['parentID'] = parentID
            titles.append(title)
            # print(headId, current, parentID)
            preCurrent = current
            headId += 1
    # print(titles)
    return titles


def writeFile(datas):
    jsObj = json.dumps(datas)  
    fileObject = open('output/jsonFile.json', 'w')  
    fileObject.write(jsObj)  
    fileObject.close()  


# def addAnchorMark(titles, planId):
#     filename = os.path.join(os.getcwd(), "html", "planReport_" + str(planId) + ".html")
#     anchorHtml = u''
#     with open(filename, 'r') as f:
#         for i in f.readlines():
#             for title in titles:
#                 old = '>' + title['FunName'] + '<'
#                 new = " id='a_" + str(
#                     title['FunID']) + "'>" + title['FunName'] + "<"
#                 old = old.replace("\r", "")
#                 i = i.replace(old, new)
#             anchorHtml += i.decode('utf8')
#     return anchorHtml


if __name__ == "__main__":
    writeFile(getMenu())

