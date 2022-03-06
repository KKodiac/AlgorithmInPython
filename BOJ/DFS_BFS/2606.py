# BOJ 2606번 문제: 바이러스
from collections import defaultdict
from collections import deque


def solution():
    number_of_computers = int(input())
    ROOT_NODE = 1
    number_of_connected_pairs = int(input())
    network = defaultdict(set)
    for _ in range(number_of_connected_pairs):
        key1, key2 = map(int, input().split())
        k_1 = list(network[key1])
        k_2 = list(network[key2])
        k_1.append(key2)
        k_2.append(key1)
        network[key1] = set(k_1)
        network[key2] = set(k_2)

    wormed = bfs(network, ROOT_NODE)
    print(len(wormed)-1)

def bfs(graph, root):
    visited = list()
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
        
    return visited
        


if '__main__' == __name__:
    solution()