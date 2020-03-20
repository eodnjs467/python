# https://www.acmicpc.net/problem/7576
# 1. 먼저 익은 토마토는 queue 에 넣는다
# 2. queue 안의 토마토를 앞에서부터 pop
# 3. 뽑아낸 토마토의 상하 좌우에 안익은 토마토가 있으면 현재까지 토마토 날에 +1
# 4. while 문을 모두 돈 뒤 0이 있으면 -1 출력, 없다면 배열내의 최댓값 -1


import sys, copy
from collections import deque

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
matrix_ck = copy.deepcopy(matrix)
queue = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] ==1:
            queue.append([i, j])

while queue:
    [i, j] = queue.popleft()
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for w in range(4):
        xx, yy = dx[w]+i, dy[w]+j
        if (0 <= xx < n) and (0 <= yy < m) and matrix_ck[xx][yy] == 0:
            matrix_ck[xx][yy] = matrix_ck[i][j] + 1
            queue.append([xx, yy])
answer = True
for row in matrix_ck:
    if 0 in row:
        print(-1)
        answer = False
        break
if answer:
    min_days = 0
    for row in matrix_ck:
        min_days = max(min_days, max(row))
    print(min_days-1)
