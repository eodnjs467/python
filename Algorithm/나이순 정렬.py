# https://www.acmicpc.net/problem/10814

import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(sys.stdin.readline().split()))
lst.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(lst[i][0], lst[i][1])

# import sys 를 사용하여 sys.stdin.readline()  사용법을 잇혔다.