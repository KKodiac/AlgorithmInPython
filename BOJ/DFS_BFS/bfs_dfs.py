# Regular implementation of BFS and DFS
# BFS uses Queue
from collections import deque

def BFS(graph, root):
    queue = deque([root])
    visited = []

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited


# DFS uses Stack
def DFS(graph, root):
    stack = [root]
    visited = []

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return visited


if '__main__' == __name__:
    root_node = 1
    graph_list= {
        1: set([2, 3]),
        2: set([1, 4]),
        3: set([1]),
        4: set([2, 5, 6]),
        5: set([4]),
        6: set([4])
    }

    print(BFS(graph_list, root_node))
    print(DFS(graph_list, root_node))
