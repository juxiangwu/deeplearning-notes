# -*- coding: utf-8 -*-

from types import MethodType

class Person:
    pass

def set_age(self,age):
    self.age = age

p = Person()
p.name = 'ABC'
print(p.name)

p.set_age = MethodType(set_age,p)
p.set_age(28)
print(p.age)

class Student:
    __slots__ = ('name','age')

s = Student()
s.age = 28
s.name = 'KK'
print(s.age,s.name)


