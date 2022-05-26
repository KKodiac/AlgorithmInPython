from collections import defaultdict
import sys 
def solution():
    N, M = map(int, input().split())
    answer = 0
    S = defaultdict(int)
    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        S[s] = 1
    for _ in range(M):
        q = sys.stdin.readline().rstrip()
        answer += S[q]

    print(answer)

if '__main__' == __name__:
    solution() 