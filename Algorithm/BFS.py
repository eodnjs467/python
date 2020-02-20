graph = {'A':['B', 'C'], 'B':['A', 'D'], 'C':['A', 'G', 'H', 'I'], 'D':['B', 'E', 'F'],
         'E':['D'], 'F':['D'], 'G':['C'], 'H':['C'], 'I':['C', 'J'], 'J':['I']}

def bfs(graph, start_node):
    visited, need_visit = [], []
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

bfs(graph, 'A')