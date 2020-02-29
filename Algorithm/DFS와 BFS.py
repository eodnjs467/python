# https://www.acmicpc.net/problem/1260
# N : 정점의 개수, M : 간선의 개수, V: 탐색 시작정점 번호

N, M, V = list(map(int, input().split()))
matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1
def dfs(current_node, row, foot_prints):
    foot_prints +=[current_node]
    for serch_noode in range(len(row[current_node])):
        if row[current_node][serch_noode] and serch_noode