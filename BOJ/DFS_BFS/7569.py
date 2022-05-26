# BOJ 7569번 문제: 토마토
# Using BFS because its more efficient in finding solutions nearby a source
from collections import deque
def solution():
    M, N, H = map(int, input().split())
    box = []

    dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
    answer = 0

    for h in range(H):
        layer = []
        for n in range(N):
            row = list(map(int, input().split()))
            layer.append(row)
        box.append(layer)

    queue = deque([])
    for ___ in range(H):
        for _ in range(N):
            for __ in range(M):
                if box[___][_][__] == 1:
                    queue.append([___, _, __])

    while queue:
        z, x, y = queue.popleft()
        for j in range(6):
            nz, nx, ny = dz[j] + z, dx[j] + x, dy[j] + y
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append([nz, nx, ny])

    for i in box:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit(0)
            answer = max(answer, max(j))

    print(answer - 1)

if '__main__' == __name__:
    solution()