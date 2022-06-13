def solution():
    a, b, c = map(int, input().split())
    if b == c:
        break_even = -1
    else:
        break_even = a // (c - b) + 1
    if break_even < 0:
        print(-1)
    else:
        print(break_even)

if '__main__' == __name__:
    solution()
