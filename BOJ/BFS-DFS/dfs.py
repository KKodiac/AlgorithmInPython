# DFS(Depth First Search) Implementaton in Python
# DFS uses stack as data structure
# Thus we use 'list' data type

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return visited


if '__main__' == __name__:
    """
        1
       / |
       2 6
      /  
      3
     /|
    4 5   그래프의 구조는 이러하다고 가정합니다.
    """
    graph_list = {1: set([2, 6]),
                  2: set([1, 3]),
                  3: set([2, 4, 5]),
                  4: set([3]),
                  5: set([3]),
                  6: set([1])}
    root_node = 1  # 시작 노드

    print(DFS(graph_list, root_node))
