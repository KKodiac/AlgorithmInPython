# BOJ 15649번 문제: N과 M (3)
from itertools import product

def solution():
    N, M = map(int, input().split())

    for i in product(range(1, N+1), repeat=M):
        print(*i)


if '__main__' == __name__:
    solution()
