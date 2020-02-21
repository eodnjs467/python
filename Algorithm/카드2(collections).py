# https://www.acmicpc.net/problem/2164

import collections
N = int(input())
deq = collections.deque([i for i in range(1, N+1)])

while len(deq) != 1:                            # 1 이 아닌동안 와일문 수행
    deq.popleft()
    deq.rotate(-1)
print(int(deq[0]))


# collections 의 사용 법을 몰랐음  collections를 사용하여 시간복잡도가 O(n) 이 되서 해결됨
# 원래 코드 . .  queue를 import 해서 put 과 get 를 써봤지만 시간 초과
# https://excelsior-cjh.tistory.com/96              -> collections.deque 사용법
# N = int(input())
# queue = [i for i in range(1, N +1)]
#
# for i in range(N-1):
#     queue.pop(0)
#     if len(queue) ==1 :
#         print(int(queue[0]))
#     tmp = queue.pop(0)
#     queue.append(tmp)