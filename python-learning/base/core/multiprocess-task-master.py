# -*- coding: utf-8 -*-

import time,random,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable = lambda: task_queue)
QueueManager.register('get_result_queue',callable = lambda: result_queue)

manager = QueueManager(address=('',5000),authkey=b'abc')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.random(1,1000)
    print('put task %d ... ' %(n))
    task.put(n)

print('Try get results...')

for i in range(10):
    r = result.get(timeout=10)
    print('result = %s' % (r))

manager.shutdown()
print('master exit')

