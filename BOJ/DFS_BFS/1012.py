# BOJ 1012 유기농 배추
from collections import deque, defaultdict
import sys
def solution():
    def bfs(graph, root, N):
        visited = [0] * (N+1)
        queue = deque([root])
        visited_index = 0
        while queue:
            n = queue.popleft()
            if not visited[n]:
                visited_index += 1
                visited[n] = visited_index
                for node in graph[n]:
                    if not visited[node]:
                        queue.append(node)

        return visited


    t = int(sys.stdin.readline().rstrip())
    m, n, k = map(int, sys.stdin.readline().rstrip().split(()))

    graph = defaultdict(list)

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)

    for 


if '__main__' == __name__:
    solution()