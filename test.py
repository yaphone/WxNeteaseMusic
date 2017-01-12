#coding=utf-8
import threading, time

L = [1, 2, 3, 4]

def test():
    t1 = threading.Thread(target=fun1, name="fun1")
    t2 = threading.Thread(target=fun2, name="fun2")
    t2.start()
    t2.join()
    t1.start()


def fun1():
    while True:
        print 1
        time.sleep(1.01)

def fun2():
    i = 0
    while i < 5:
        print 2
        i += 1
        time.sleep(1.02)


if __name__ == '__main__':
    test()