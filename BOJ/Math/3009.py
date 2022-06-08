# BOJ 3009  네번째 점
def solution():
    answer_x = []
    answer_y = []

    for _ in range(2):
        x, y = map(int, input().split())
        answer_x.append(x)
        answer_y.append(y)

    dx, dy = map(int, input().split())
    ax = ay = 0
    if dx in answer_x:
        answer_x.remove(dx)
        ax = answer_x.pop()
    else:
        ax = dx
    if dy in answer_y:
        answer_y.remove(dy)
        ay = answer_y.pop()
    else:
        ay = dy

    print(ax, ay)


if '__main__' == __name__:
    solution()



