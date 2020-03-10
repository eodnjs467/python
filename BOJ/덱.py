# https://www.acmicpc.net/problem/10866

from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    word = sys.stdin.readline().split()
    if word[0]=='push_front':
        q.appendleft(word[1])
    elif word[0]=='push_back':
        q.append(word[1])
    elif word[0] == 'pop_front':
        if len(q)==0: print(-1)
        else: print(q.popleft())
    elif word[0] == 'pop_back':
        if len(q)==0: print(-1)
        else: print(q.pop())
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    elif word[0] == 'front':
        if len(q) == 0: print(-1)
        else: print(q[0])
    elif word[0] == 'back':
        if len(q) == 0: print(-1)
        else: print(q[-1])