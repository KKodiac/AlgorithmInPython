# BOJ 15649번 문제: N과 M (4)
from itertools import combinations

def solution():
    N, M = map(int, input().split())

    for i in combinations(range(1, N+1), M):
        print(*i)



if '__main__' == __name__:
    solution()
