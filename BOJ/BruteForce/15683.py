# BOJ 15683 감시
import copy
def solution():
    n, m = map(int, input().split())
    sights = {
        1: [[0], [1], [2], [3]],
        2: [[0, 2], [1, 3]],
        3: [[0, 1], [1, 2], [2, 3], [3, 0]],
        4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        5: [[0, 1, 2, 3]]
    }
    room = [list(map(int, input().split())) for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def area(x, y, sights, graph):
        for sight in sights:
            nx, ny = x, y
            while True:
                nx += direction[sight][0]
                ny += direction[sight][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 6:  # Wall
                    break
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'

    def dfs(n, graph):
        global answer
        tmp = copy.deepcopy(graph)
        if n == len(cctv):
            count = 0
            for g in tmp:
                count += g.count(0)
            answer = min(answer, count)
            return

        x, y, cam = cctv[n]
        for sight in sights[cam]:
            area(x, y, sight, tmp)
            dfs(n + 1, tmp)
            tmp = copy.deepcopy(graph)

    cctv = []

    for i in range(n):
        for j in range(m):
            if 0 < room[i][j] < 6:
                cctv.append((i, j, room[i][j]))

    dfs(0, room)


if '__main__' == __name__:
    answer = 10000000000
    solution()
    print(answer)