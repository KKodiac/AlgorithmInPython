# BOJ 10845 번 문제: 큐
from sys import stdin
from collections import deque
def solution():
    N = int(input())
    queue = deque()
    for _ in range(N):
        command = stdin.readline().split()
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(int(not queue))
        elif command[0] == 'front':
            if queue:
                print(queue[0])
            else: 
                print(-1)
        elif command[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
            

if '__main__' == __name__:
    solution()