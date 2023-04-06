#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
https://www.runoob.com/python/python-xml.html

SAX是一种基于事件驱动的 API。
利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器。
解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
而事件处理器则负责对事件作出响应，对传递的XML数据进行处理。
1、对大型文件进行处理；
2、只需要文件的部分内容，或者只需从文件中得到特定信息。
3、想建立自己的对象模型的时候。
在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。

ContentHandler类方法介绍
characters(content)方法
    调用时机：
    从行开始，遇到标签之前，存在字符，content 的值为这些字符串。
    从一个标签，遇到下一个标签之前， 存在字符，content 的值为这些字符串。
    从一个标签，遇到行结束符之前，存在字符，content 的值为这些字符串。
    标签可以是开始标签，也可以是结束标签。

startDocument() 方法：文档启动的时候调用。
endDocument() 方法：解析器到达文档结尾时调用。
startElement(name, attrs)方法：遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
endElement(name) 方法：遇到XML结束标签时调用。
'''
import xml.sax


class xmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = xmlHandler()
    parser.setContentHandler(Handler)

    parser.parse("../../data/testxml.xml")