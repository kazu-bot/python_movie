import collections
import queue

#Double-end queue
collections.deque

#queueはリストと同じような使い方ができるよ
#メモリ効率がリストよりも良いので、重いリスト作るよりもqueue使用した方が早くなるよ
q = queue.Queue()
lq = queue.LifoQueue() #[0,1,2]
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

for _ in range(3):
    print('FIFO queue = {}'.format(q.get()))
    print('LIFO queue = {}'.format(lq.get()))
    print('list       = {}'.format(l.pop(0)))
    print('deque      = {}'.format((d.popleft())))
    print()
