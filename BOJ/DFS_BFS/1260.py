# BOJ 1260번 문제: DFS와 BFS
from collections import deque
from collections import defaultdict
N, M, V = map(int, input().split())

temp = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    temp[a].append(b)
    temp[b].append(a)

grapha = defaultdict(set)

for i in temp.keys():
    grapha[i] = set(temp[i])

def dfs(graph, root):
    visited = list()
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            temp = list(graph[n] - set(visited))
            temp.sort(reverse=True)
            stack += temp


    return visited

def bfs(graph, root):
    visited = list()
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            temp.sort()
            queue += temp


    return visited


print(*dfs(grapha, V))
print(*bfs(grapha, V))
