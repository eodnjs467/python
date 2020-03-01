# https://www.acmicpc.net/problem/2667

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
def dfs(matrix, cnt, x, y):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    matrix[x][y] = 0

    for w in range(4):
        n_x, n_y = x + dx[w], y + dy[w]
        if n_x>=0 and n_x<N and n_y >=0 and n_y<N:
            if matrix[n_x][n_y] == 1:
                cnt = dfs(matrix, cnt+1, n_x, n_y)
    return cnt
# ------------------------------------------------------------------

N = int(input())
