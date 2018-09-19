# 1. github版本pyMd2Doc介紹


# 2. 使用方法
该程序所需python环境为python3或以上。

## 2.1 准备Markdown文件
将准备好需要转成文档的Markdown文件复制粘贴到pyMd2Doc/app/title.md文件中，保存。

## 2.2 修改启动配置
打开start.bat文件，修改python环境安装位置和当前项目存在位置。

## 2.3 开始转换
双击执行start.bat文件，该文件做了两部操作
安装需要的依赖
将Markdown文件转换成带目录结构的文档

## 2.4 查看文档
用浏览器打开刚刚生成的title.html文件。
点击目录可以跳转到相应文档内容。


# 1. pip 安装版本pyMd2Doc介紹
利用python将markdown转换成带可收缩,可跳转到文本内容的目录文档。

# 2. 使用方法
该程序所需python环境为python3或以上。

## 2.1 准备Markdown文件
准备好需要转成文档的Markdown文件。

## 2.2 安装pyMd2Doc
用pip install pyMd2Doc 安装程序

## 2.3 开始转换
> 新建[yourFileName].py文件,准备所需要转换的markdown文件，如myMarkdown.md
> 引入所需模块,调用函数并传入需要转换的markdown文件，如下示例：

''' python

#固定写法，需要引用pyMd2Doc的模块
from pymd2doc import createDoc

# 要转换的markdown文件，如myMarkdown.md
#双引号内为要转换的markdown文件名称
createDoc.create("myMarkdown")

'''
> 执行成功后会生成myMarkdown.html文件


## 2.4 查看文档
用浏览器打开刚刚生成的myMarkdown.html文件。
点击目录可以跳转到相应文档内容。
