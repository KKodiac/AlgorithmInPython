# BOJ 5430번 문제: AC
from collections import deque
import sys
def solution():
    T = int(sys.stdin.readline())

    for _ in range(T):
        func_p = str(sys.stdin.readline())
        n = int(sys.stdin.readline())
        a = deque(eval(sys.stdin.readline()))

        if n < func_p.count('D'):
            print('error')
            continue
        
        r_cnt = 0
        for p in func_p:
            if p == 'R':
                r_cnt += 1

            elif p == 'D':
                if r_cnt % 2 == 1:
                    a.pop()
                else:
                    a.popleft()
        
        if r_cnt % 2 == 1:
            a.reverse()

        print(list(a))

if '__main__' == __name__:
    solution()