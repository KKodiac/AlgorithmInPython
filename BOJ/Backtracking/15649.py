# BOJ 15649번 문제: N과 M (1)
from itertools import permutations

def solution():
    N, M = map(int, input().split())

    for i in permutations(list(range(1, N+1))):
        print(*i)


if '__main__' == __name__:
    solution()
