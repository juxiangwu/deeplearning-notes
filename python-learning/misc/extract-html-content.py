# -*- coding: utf-8 -*-
'''
抽取HTML文档内容
'''
from lxml import etree,html

path = 'temp/test.html'

content = open(path,'rb').read()

page = html.document_fromstring(content)

text = page.text_content()
print(text)