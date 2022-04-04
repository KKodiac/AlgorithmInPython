# BOJ 1439번 문제: 뒤집기
def solution():
    S = input()
    x = S.split(sep='0')
    y = S.split(sep='1')
    xs = 0
    ys = 0
    for i in x:
        if not i == '':
            xs += 1

    for j in y:
        if not j == '':
            ys += 1

    print(min(xs, ys))

if '__main__' == __name__:
    solution()