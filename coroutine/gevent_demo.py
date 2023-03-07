from gevent import monkey
import gevent
import time

monkey.patch_all()  #将模块里的IO接口替换成gevent自己的非阻塞IO接口，如time模块，sokect模块

def fun1(a, b):
    print(a)
    time.sleep(2)
    print(b)


def fun2(a, b):
    print(a)
    time.sleep(2)
    print(b)


def gevent_test():
    # 协程函数之间不能有依赖
    gevent.joinall([
        gevent.spawn(fun1, 1, 2),
        gevent.spawn(fun1, 3, 4)
    ])


if __name__ == '__main__':
    gevent_test()
