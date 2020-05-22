# 処理の並列化(デーモンスレッド)
# デーモンスレッド：デーモン化したスレッドは、起動状態であってもプログラムが終了した時点で、強制終了してしまう
# デーモン化したスレッドの処理の完了を待って、プログラムを終了させたいときは、join 関数を使用する必要がある。

# ついでにタイマーも。

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


def worker2():
    logging.debug('start worker2')
    time.sleep(2)
    logging.debug('end worker2')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    # setDaemonにてデーモンスレッド化する。
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
    t1.join()

    logging.debug('****************************')
    # 同関数にて複数スレッドを起動することもできる。
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    logging.debug('############################')
    # 上記をenumerateで書くこともできる。むしろこっちのほうが楽か
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
    for thread in threading.enumerate():
        if thread is threading.current_thread():
            print(thread)
            continue
        thread.join()

    # タイマー処理を少しまってからスタートさせる。
    t = threading.Timer(interval=3, function=worker1, args=(100,), kwargs={'y': 200})
    t.start()
