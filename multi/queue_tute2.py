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
        queue.task_done()

    logging.debug('logggggggggggg')
    logging.debug('end worker1')


def worker2(queue):
    logging.debug('start worker2')
    time.sleep(2)
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end worker2')


if __name__ == '__main__':
    queue = queue.Queue()
    #タスク大量実行
    for i in range(1000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t=threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)

    # quwueにmainでNoneを詰める
    logging.debug('tasks are not done')
    queue.join()

    #worker1の処理が長かったりした場合、worker1側に「queue.task_done()」を入れてやることで
    #処理の終了を待たずして並列処理が可能
    logging.debug('tasks are done')

    #作成したスレッド分Noneを入れてやる
    for _ in range(len(ts)):
        queue.put(None)