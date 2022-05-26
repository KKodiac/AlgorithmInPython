import sys
from collections import deque, defaultdict

def solution():
    """ Tree 형태가 아니라 그냥 Graph 형태만으로 생각해도 되었던 문제 였습니다. """

    input = sys.stdin.readline
    n = int(input())
    family_one, family_two = map(int, input().split())
    m = int(input())
    family_tree = defaultdict(list)

    for _ in range(m):
        parent, child = map(int, input().split())
        family_tree[parent].append(child)
        family_tree[child].append(parent)

    def bfs(graph, start, end):
        depth = 0
        queue = deque([[start, depth]])
        visited = list()
        while queue:
            n = queue.popleft()
            member = n[0]
            depth = n[1]
            if member == end:
                return depth
            if member not in visited:
                depth += 1
                visited.append(member)
                for child in graph[member]:
                    if child not in visited:
                        queue.append([child, depth])

        return -1

    print(bfs(family_tree, family_one, family_two))


if '__main__' == __name__:
    solution()