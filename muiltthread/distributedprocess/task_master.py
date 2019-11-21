import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue", callable=lambda :task_queue)
QueueManager.register("get_result_queue", callable=lambda :result_queue)
# bind port 5000,setup verification code
manager = QueueManager(address=("",5000),authkey=b"abc")
# start Queue
manager.start()
# get the object visited by internet
task = manager.get_task_queue()
result = manager.get_result_queue()

# put some tasks in in it
for i in range(10):
    n = random.randint(0, 1000)
    print("Put task %d..." % n)
    task.put(n)
# get result from result queue
print("try get result")
for i in range(10):
    r = result.get(timeout=10)
    print("Result: %s" % r)
# close manager
manager.shutdown()
print("master exit.")




