# -*- coding: utf-8 -*-
import re
import os
import json
import markdown
import codecs

pattern = '#+\s'

heading = {
        'heading1': 0,
        'heading2': -1,
        'heading3': -1,
        'heading4': -1,
        'heading5': -1,
        'heading6': -1
    }

htmlHead = u'''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script src="../app/static/js/jquery-3.2.1.js"></script>
<script src="../app/static/js/main.js"></script>
<link href="../app/static/css/main.css" rel="stylesheet" />
</head>
<title>markdown转文档</title>
</head>
<body>
    <div class="content">
        <div class="parentnode"></div>
        <div class="right">
'''

htmlTail = u'''
</body>
</html>
 '''


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


def getMenu(filename):
    titles = []
    global heading
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


def addAnchorMark(titles, name):
    filename = os.path.join(os.getcwd(), "html", name + ".html")
    anchorHtml = u''
    with open(filename, 'r', encoding='UTF-8') as f:
        for i in f.readlines():
            for title in titles:
                old = '>' + title['titleName'] + '<'
                new = " id='a_" + str(
                    title['titleID']) + "'>" + title['titleName'] + "<"
                old = old.replace("\r", "")
                i = i.replace(old, new)
            anchorHtml += i
    # print(anchorHtml)
    out_file = '%s.html' % (name)
    output_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(anchorHtml)
    output_file.close()
    return anchorHtml


def convertHtml(filename, json):
    in_file = '%s.md' % (filename)
    out_file = '%s.html' % (filename)
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    output_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    
    htmlJson = u" </div> </div><input style='display: none' id='jsonContent' value='"+ json  +"'></input>"
    output_file.write(htmlHead+html+htmlJson+htmlTail)
    output_file.close()


if __name__ == "__main__":
    filename = os.getcwd() + '/title.md'
    # 解析markdown层级目录关系
    # getMenu(filename)
    # markdown转html（生成html）
    convertHtml(os.getcwd() + '/title', json.dumps(getMenu(filename)))
    # 给html加锚标记
    addAnchorMark(getMenu(filename), os.getcwd() + '/title')
