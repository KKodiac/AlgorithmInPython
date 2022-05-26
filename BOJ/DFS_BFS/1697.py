# BOJ 1697번 문제: 숨바꼭질
from collections import deque

def solution():
    N, K = map(int, input().split())

    queue = deque([N])
    visited = [0] * 100001
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break
        for i in [x-1, x+1, x*2]:
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)


if '__main__' == __name__:
    solution()
