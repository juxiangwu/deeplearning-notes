# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue 
import os,random,time

def write_proc(q):
    print('Process to write:%s' % (os.getpid()))
    for value in ['A','B','C','D','E','F']:
        print('Put %s to queue ...' % (value))
        q.put(value)
        time.sleep(random.random())

def read_proc(q):
    print('Process to read:%s' % (os.getpid()))
    while True:
        value = q.get(True)
        print('Get from queue:%s' % (value))

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write_proc,args = (q,))
    pr = Process(target=read_proc,args = (q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
    print('All process end')