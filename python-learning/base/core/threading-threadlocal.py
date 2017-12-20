# -*- coding: utf-8 -*-

import threading

local_scool = threading.local()

def process_student():
    std = local_scool.student
    print('Hello %s in %s ' %(std,threading.current_thread().name))

def process_thread(name):
    local_scool.student = name
    process_student()


t1 = threading.Thread(target=process_thread,args = ('Alice',))
t2 = threading.Thread(target=process_thread,args = ('Bob',))

t1.start()
t2.start()

t1.join()
t2.join()

