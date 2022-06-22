def solution():
    x, y, w, h = map(int, input().split())
    print(min(x, y, w - x, h - y))

if '__main__' == __name__:
    solution()