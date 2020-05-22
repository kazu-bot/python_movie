# キューの使用方法

import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

#worker1でキューに100積める→worker2でget
#worker2はキューが空の状態のため、値が積められるまで待ちが発生
#worker1が値を積めたらworker2が値を取得して出力
def worker1(queue):
    logging.debug('start worker1')
    queue.put(100)  #[100,200]
    time.sleep(5)
    queue.put(200)
    logging.debug('end worker1')


def worker2(queue):
    logging.debug('start worker2')
    time.sleep(2)
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end worker2')


if __name__ == '__main__':
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue,))
    t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    t2.start()
