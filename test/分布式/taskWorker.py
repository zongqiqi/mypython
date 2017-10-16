import time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='127.0.0.1'
print('Connect to server %s ...'%server_addr)
m=QueueManager(address=(server_addr,8001),authkey=b'key')
m.connect()
task=m.get_task_queue()
result=m.get_result_queue()
while (not task.empty()):
	image_url=task.get(True,timeout=5)
	print('run task download %s ...'%image_url)
	time.sleep(1)
	result.put('$s ---> success '%image_url)
print('worker exit')