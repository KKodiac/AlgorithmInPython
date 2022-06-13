# BOJ 2869 달팽이는 올라가고 싶다
def solution():
    a, b, v = map(int, input().split())
    days = (v - b - 1) // (a - b) + 1

    print(days)

if '__main__' == __name__:
    solution()