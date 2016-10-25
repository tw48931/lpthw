# codingutf-8
import random
import Queue
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support   # 不用加也可以正常启动服务器


# 当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对
# 原始的task_queue进行操作，那样就绕过了QueueManager的封装，
# 必须通过manager.get_task_queue()获得的Queue接口添加。


# 发送任务的队列
task_queue = Queue.Queue()

# 接收结果的队列
result_queue = Queue.Queue()


# ??modified
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 注册到网络
# modified
def start_server():
    # modified
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    # register内不要使用lambda，否则win7运行出错
    # callable=lambda: task_queue => callable=return_task_queue
    # callable=lambda: result_queue => callable=return_result_queue
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    #

    # 绑定端口5000，设置验证码'abc'
    # win7 需要写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey='abc')

    # 启动Queue
    manager.start()

    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果
    print('Try get results...')
    # 服务器已经准备好接收数据，故开始启动task_worker.py
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except Queue.Empty:     # Queue.Empty => queue.Empty
            print('result queue is empty.')

    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    start_server()