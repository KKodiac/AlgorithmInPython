import sys

def solution():
    N = int(sys.stdin.readline())
    mem = [0] * 10001
    for _ in range(N):
        num = int(sys.stdin.readline())
        mem[num] += 1
    
    for idx, val in enumerate(mem):
        if idx > 0:
            for i in range(val):
                print(idx)
        

if '__main__' == __name__:
    solution()