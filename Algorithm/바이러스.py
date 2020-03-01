# https://www.acmicpc.net/problem/2606

computer = int(input())
network = int(input())
virus_map = [[0 for _ in range(computer+1)] for _ in range(computer+1)]

for _ in range(network):
    x, y = map(int, input().split())
    virus_map[x][y] = 1
    virus_map[y][x] = 1

def bfs(virus_map, start):
    queue = [start]
    visited = []

    while queue:
        temp = queue.pop(0)
        visited.append(temp)

        for i in range(len(virus_map)):
            if virus_map[temp][i] and i not in visited and i not in queue:      # virus_map[temp][i]==1 생략 됨.
                print(queue, temp)                                              # if !ck: , if ck: 사용 가능.
                queue.append(i)
    return len(visited)-1

print(bfs(virus_map, 1))