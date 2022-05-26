# BOJ 10866번 문제: 덱
from collections import deque
from sys import stdin
def solution():
    dequeue = deque()

    N = int(stdin.readline()) # 1 <= N <= 10000
    for _ in range(N):
        command = stdin.readline().split()
        if command[0] == 'push_back':
            dequeue.append(int(command[1]))
        elif command[0] == 'push_front':
            dequeue.appendleft(int(command[1]))
        elif command[0] == 'pop_front':
            if len(dequeue):
                print(dequeue.popleft())
            else:
                print(-1)
        elif command[0] == 'pop_back':
            if len(dequeue):
                print(dequeue.pop())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(dequeue))
        elif command[0] == 'empty':
            print(int(not len(dequeue)))
        elif command[0] == 'front':
            if len(dequeue):
                print(dequeue[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if len(dequeue):
                print(dequeue[-1])
            else:
                print(-1)


if '__main__' == __name__:
    solution()