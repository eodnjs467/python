# https://www.acmicpc.net/problem/10828

import sys

N = int(sys.stdin.readline())
ans = []

for _ in range(N):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        ans.append(word[1])
    elif word[0] == 'pop':
        if len(ans)==0:
            print(-1)
        else: print(ans.pop())
    elif word[0] == 'size':
        print(len(ans))
    elif word[0] == 'empty':
        if len(ans)==0:
            print(1)
        else: print(0)
    elif word[0] == 'top':
        if len(ans)==0:
            print(-1)
        else: print(ans[-1])