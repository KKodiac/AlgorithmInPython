# BOJ 2164번 문제: 카드2
from collections import deque
def solution():
    N = int(input())

    stack = deque(list(range(N, 0, -1)))
    while len(stack) != 1:
        stack.pop()
        stack.appendleft(stack.pop())
    
    print(stack.pop())


if '__main__' == __name__:
    solution()