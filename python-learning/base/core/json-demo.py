# -*- coding: utf-8 -*-

import json

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(s):
    return {
        'name':s.name,
        'age':s.age,
        'score':s.score
    }

def dict2student(s):
    return Student(s['name'],s['age'],s['score'])

d = dict(name="Bob",age=24,score=80)
print(json.dumps(d))

json_str = '{"name":"jenson","age":28,"score":99}'
obj = json.loads(json_str)
print(obj)
s = Student('kkoolerter',30,99)
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

std = json.loads(json_str,object_hook=dict2student)
print(std.name,std.age,std.score)