# BOJ 11651 좌표 정렬하기 2
def solution():
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x,y))
    coords = sorted(coords, key=lambda v: (v[1], v[0]))
    for i in coords:
        print(i[0], i[1])


if '__main__' == __name__:
    solution()