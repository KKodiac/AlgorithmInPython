from collections import deque
from sys.stdin import readline

def main():
    queue = deque()

    commands = int(input())
    while commands > 0:
        command = readline().split()
        if command[0] == "push":
            queue.append(command[1])
        elif command[0] == "pop":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
        elif command[0] == "size":
            print(len(queue))
        elif command[0] == "empty":
            if not len(queue):
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if len(queue):
                print(queue[0])
            else:
                print(-1)
        elif command[0] == "back":
            if len(queue):
                print(queue[-1])
            else:
                print(-1)

        commands -= 1


if '__main__' == __name__:
    main()
