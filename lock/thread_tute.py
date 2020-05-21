#処理の並列化
#Threadを用いることで処理を並列化させることが可能。
#下記実行により、worker1とworker2が同時処理となっていることが分かるようにloggingとsleepを入れた
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def worker1():
    logging.debug('start worker1')
    time.sleep(5)
    logging.debug('end worker1')

def worker2(x,y=1):
    logging.debug('start worker2')
    logging.debug(x)
    logging.debug(y)

    time.sleep(2)
    logging.debug('end worker2')

if __name__ == '__main__':
    t1 = threading.Thread(name='rename worker1', target=worker1)
    t2 = threading.Thread(target=worker2,args=(100,), kwargs={'y':200})
    t1.start()
    t2.start()
    print('started')