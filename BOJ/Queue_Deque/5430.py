# BOJ 5430번 문제: AC
from collections import deque
import sys
def solution():
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        p = str(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        x = deque(sys.stdin.readline()[1:-2].rstrip().split(','))
        if n == 0:
            x = []
        is_valid = True
        R = 0
        for i in p:
            if i == 'R':
                R += 1
            if i == 'D':
                if x:
                    if R % 2:
                        x.pop()
                    else:
                        x.popleft()
                else:
                    is_valid = False
                    break
        if not is_valid:
            print('error')
            continue
        
        if R % 2:
            x = reversed(x)

        print("["+",".join(i for i in x)+"]")

                

if '__main__' == __name__:
    solution()