# BOJ 7576번 문제: 토마토
# Using BFS because its more efficient in finding solutions nearby a source
from collections import deque
def solution():
    M, N = map(int, input().split())
    box = []

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0

    for i in range(N):
        row = list(map(int, input().split()))
        box.append(row)

    queue = deque([])
    for _ in range(N):
        for __ in range(M):
            if box[_][__] == 1:
                queue.append([_, __])

    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx, ny = dx[j] + x, dy[j] + y
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

    for i in box:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(i))

    print(answer - 1)

if '__main__' == __name__:
    solution()