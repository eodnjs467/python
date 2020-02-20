graph = {'A':['B', 'C'], 'B':['A', 'D'], 'C':['A', 'G', 'H', 'I'], 'D':['B', 'E', 'F'],
         'E':['D'], 'F':['D'], 'G':['C'], 'H':['C'], 'I':['C', 'J'], 'J':['I']}
def dfs(graph, start_node):
    visited, need_visited = [], []
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

dfs(graph, 'A')