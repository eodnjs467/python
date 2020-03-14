# https://www.acmicpc.net/problem/7576

# 1 : 익은 토마토, 0 : 익지않은 토마토, -1 : 토마토x
# 전부 0 이거나 -1이 막고있으면 익지못함

m, n = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
test_matrix = [[0 for _ in range(m)]for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0

for i in range(n):
    for j in range(m):
        for w in range(4):
            ii, jj = dx[w]+i, dy[w]+j
            if matrix[i][j]==1 and matrix[ii][jj]!=-1:
                matrix[ii][jj] = 1
                # test_matrix[ii][jj] = 1
                cnt+=1
            elif matrix[i][j]==-1:
                if -1 in matrix[ii][jj]:
                    print(0)
                    break
                continue
print(cnt)