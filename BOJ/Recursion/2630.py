# BOJ 2630번 문제: 색종이 만들기
N = int(input())
paper = list()
answer = []
for i in range(N):
    line = list(map(int, input().split()))
    paper.append(line)


def divide(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                divide(x, y, N//2)
                divide(x, y+N//2, N//2)
                divide(x+N//2, y, N//2)
                divide(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        answer.append(0)
    else:
        answer.append(1)

divide(0, 0, N)
print(answer.count(0))
print(answer.count(1))
