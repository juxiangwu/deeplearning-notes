# -*- coding: utf-8 -*-
import hashlib

md5 = hashlib.md5()
md5.update('hello world'.encode('utf-8'))
print(md5.hexdigest())

md5.update('hello,python,world'.encode('utf-8'))
md5.update('hello,pthon,world'.encode('utf-8'))
print(md5.hexdigest())