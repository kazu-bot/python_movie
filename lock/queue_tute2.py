# キューの使用方法（キューから値が取得できない場合の抜け方の例）
# main側for loopで値を詰めて最後にNoneを積めるやり方。
# 色々な箇所で考え方として使えるため別切り出し

import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(queue):
    logging.debug('start worker1')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
    logging.debug('end worker1')


def worker2(queue):
    logging.debug('start worker2')
    time.sleep(2)
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end worker2')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)
    t1 = threading.Thread(target=worker1, args=(queue,))
    t1.start()
    # quwueにmainでNoneを詰める
    queue.put(None)
