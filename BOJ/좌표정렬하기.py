# https://www.acmicpc.net/problem/11650

import sys

n = int(sys.stdin.readline())
ans = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ans.append((x, y))

ans = sorted(ans, key=lambda x: (x[0], x[1]))
for i in ans:
    print(i[0], i[1])