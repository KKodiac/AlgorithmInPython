# BOJ 2217 로프(그리디)
def solution():
    n = int(input())
    ropes = []
    for _ in range(n):
        ropes.append(int(input()))

    value = []
    ropes.sort(reverse=True)
    for idx, rope in enumerate(ropes):
        value.append(rope * (idx+1))

    print(max(value))


if '__main__' == __name__:
    solution()