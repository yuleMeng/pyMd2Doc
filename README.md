# 1. github版本pyMd2Doc介紹
将md格式转化为html格式，可用于一般md文档转html,md电子书转html,快速制作电子书。

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
用如下命令安装程序

	pip install pyMd2Doc


## 2.3 开始转换
以下暂时提供两种转换方法

### 2.3.1 md文件转html
> 新建[yourFileName].py文件,准备所需要转换的markdown文件，如myMarkdown.md
> 引入所需模块,调用函数并传入需要转换的markdown文件，如下示例：

	from pymd2doc import createDoc
	
	# param myMarkdown 传入MD文件名（生成html默认和MD文件名一致）
	# return myMarkdown.html
	createDoc.create("myMarkdown")


> 执行成功后会生成myMarkdown.html文件,以及一个static文件夹。
> myMarkdown.html： 转换成的html内容
> static文件夹： 支持myMarkdown.html的静态文件，如js,css,icon


### 2.3.2 String型的md内容转html
> 引入所需模块,调用函数
> 传入String型的md内容，如下示例：

	from pymd2doc import createDoc
	
	str = u'''
		此处是String型的md内容
		'''
	# param strs 传入MD字符串
	# param myMarkdown 定义将要生成html文件名称
	# return myMarkdown.html
	createDoc.createByString(strs, "myMarkdown")
	
> 执行成功后会生成myMarkdown.html文件,以及一个static文件夹。
> myMarkdown.html： 转换成的html内容
> static文件夹： 支持myMarkdown.html的静态文件，如js,css,icon

## 2.4 查看文档
用浏览器打开刚刚生成的myMarkdown.html文件。
点击目录可以跳转到相应文档内容。
如果目录有子目录可以进行收缩
