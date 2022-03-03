# BFS(Breadth First Search) Implementaton in Python
# BFS uses Queue as data structure 
# Thus we need to import 'deque' from collections library
from collections import deque


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited


if '__main__' == __name__:
    """
        1
       / |
       2 3
      /  
      4
     /|
    5 6   그래프의 구조는 이러하다고 가정합니다.
    """
    graph_list = {1: set([2, 3]),
                  2: set([4]),
                  3: set([1]),
                  4: set([2, 5, 6]),
                  5: set([4, 6]),
                  6: set([4])}
    root_node = 1  # 시작 노드

    print(BFS(graph_list, root_node))
