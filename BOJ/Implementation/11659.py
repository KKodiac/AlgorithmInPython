import sys


def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    prefix = [0]

    pre_sums = 0
    for i in numbers:
        pre_sums += i
        prefix.append(pre_sums)

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        print(prefix[j] - prefix[i-1])


if '__main__' == __name__:
    solution()
