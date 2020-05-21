# 処理の並列化
# 処理中にロックを行う手法サンプル

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(d, lock):
    logging.debug('start worker1')
    # python doc
    # acquire() は他のスレッドが release() を呼出してロックの状態をアンロックに変更するまでブロックします。
    # 複数のスレッドにおいて acquire() がアンロック状態への遷移を待っているためにブロックが起きている時に
    # release() を呼び出してロックの状態をアンロックにすると、一つのスレッドだけが処理を進行できます。
    lock.acquire()
    i = d['x']
    time.sleep(5)
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end worker1')


def worker2(d, lock):
    logging.debug('start worker2')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end worker2')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.Lock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    print('started')
