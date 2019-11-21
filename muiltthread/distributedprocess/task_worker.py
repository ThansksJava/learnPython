import time,sys,queue
from multiprocessing.managers import BaseManager

SERVER_ADDR='192.168.253.131'


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")
# connect to the server endpoint
server_addr = SERVER_ADDR
print('Connect to server %s...' % server_addr)
# port and verify code must conformity with the task_master.py file
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# start connect
m.connect()
# get Queue object
task = m.get_task_queue()
result = m.get_result_queue()
# get task from queue and record the result
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')