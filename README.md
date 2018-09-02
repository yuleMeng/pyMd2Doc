
python解析Markdown内容，

```markdown
# 1.标题
## 1.1标题
### 1.1.1 标题
 内容内容内容内容内容内容内容内
### 1.1.2 标题
 内容内容内容内容内容内容内容内
### 1.1.3 标题
 内容内容内容内容内容内容内容内
# 2.标题
## 2.1标题
 内容内容内容内容内容内容内容内
```
**该文章主要功能是解析markdown标题，构建父类标题与子类标题之间的对应关系。**

## 原理概述 ##
 1. “#”个数比上一层多一个或多个，默认为上级目录的子目录。
 2. 分别记住1~6级目录的状态（父节点是否结束）。
 3. 遇到“#”没有按每次加一个的方式递进，当父节点没有结束的话，就是子节点；当父节点结束，则跳过节点查询节点目前应该到的父节点。

## 结果形式 ##
根据的格式将标题解析成如下类型，
方便发到前台生成树状可伸缩的菜单

[
{ "titleID": 1, "parentID": 0, "titleName": "1.标题" }，
{ "titleID": 2, "parentID": 1, "titleName": "1.1标题" }，
{ "titleID": 3, "parentID": 2, "titleName": "1.1.1 标题" }，
{ "titleID": 4, "parentID": 2, "titleName": "1.1.2 标题" }，
{ "titleID": 5, "parentID": 2, "titleName": "1.1.3 标题" }，
{ "titleID": 6, "parentID": 0, "titleName": "2. 标题" }，
{ "titleID": 7, "parentID": 6, "titleName": "2.1 标题" }，
......
]

``` python
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
    with open(filename, 'r') as f:
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


if __name__ == "__main__":
    writeFile(getMenu())



```

