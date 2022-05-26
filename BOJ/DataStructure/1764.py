from collections import defaultdict
import sys

def solution():
    N, M = map(int, input().split())
    names = defaultdict(int)
    answer = 0
    aname = []
    for _ in range(N):
        name = sys.stdin.readline().rstrip()
        names[name] = 1

    for _ in range(M):
        name = sys.stdin.readline().rstrip()
        if names[name] == 1:
            answer += names[name]
            aname.append(name)

    print(answer)
    for i in sorted(aname):
        print(i)

if '__main__' == __name__: 
    solution()