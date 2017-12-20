# -*- coding: utf-8 -*-

import time,threading

balance = 0
lock = threading.Lock()

def charge_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    print(balance)

def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            charge_it(n)
        finally:
            lock.release()
    
t1 = threading.Thread(target=run_thread,args = (5,))
t2 = threading.Thread(target=run_thread,args = (8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)
