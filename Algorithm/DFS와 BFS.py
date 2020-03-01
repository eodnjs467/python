# https://www.acmicpc.net/problem/1260
# N : 정점의 개수, M : 간선의 개수, V: 탐색 시작정점 번호

N, M, V = map(int, input().split())
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def dfs(matrix, V):
    stack = [V]
    visit = []

    while stack:
        tmp = stack.pop()
        visit.append(tmp)

        for i in range(len(matrix)):
            if matrix[tmp][i] and i not in stack and i not in visit:
                stack.append(i)
                break               # 꼼수 ...
    return visit

def bfs(matrix, start):
    queue = [start]
    visit = []

    while queue:
        temp = queue.pop(0)
        visit.append(temp)

        for i in range(len(matrix)):
            if matrix[temp][i] and i not in queue and i not in visit:
                queue.append(i)
    return visit

print(dfs(*matrix, V))
print(bfs(*matrix, V))





#
# N, M, V = map(int, input().split())
# matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for _ in range(M):
#     x, y = map(int, input().split())
#     matrix[x][y] = 1
#     matrix[y][x] = 1
#
# def dfs(matrix, start):
#     stack = [(start, 0)]
#     ck = [0]*(N+1)
#     ck[start] = 1
#
#     while stack:
#         tmp, idx = stack.pop()
#     for i in range(idx, len(matrix)):
#         if matrix[tmp][i]==1 and ck[i]==0:
#             ck[i] =1
#             stack.append((tmp, i+1))
#             stack.append((i, 0))
#             break
#
#     return stack
# dfs(matrix, V)

print(dfs(V, matrix))

def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

def dfs(current, matrix):
    visited = []
    visited.append(current)
    for i in range(len(matrix[current])):
        if matrix[current][i] and i not in visited:
            visited = dfs(i, matrix, visited)
    return visited

