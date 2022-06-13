# BOJ 24479 알고리즘 수업 - 깊이 우선 탐색 1
from collections import defaultdict
import sys
def solution():
    n, m, r = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    for val in graph:
        graph[val] = sorted(list(set(graph[val])), reverse=True)

    visited = dfs(graph, r, n)[1:]
    for i in visited:
        print(i)


def dfs(graph, root, N):
    stack = [root]
    visited = [0] * (N+1)
    visited_idx = 1
    while stack:
        n = stack.pop()
        if not visited[n]:
            visited[n] = visited_idx
            visited_idx += 1
            for node in graph[n]:
                if not visited[node]:
                    stack.append(node)

    return visited


if '__main__' == __name__:
    solution()