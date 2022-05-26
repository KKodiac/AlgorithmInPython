import queue


from collections import deque
def solution():
    N, K = map(int, input().split())
    queue = deque([i for i in range(1,N+1)])
    answer = []
    counter = 0
    while queue:
        n = queue.popleft()
        counter += 1
        if counter == K:
            counter = 0
            answer.append(n)
        else:
            queue.append(n)

    print("<", end="")
    print(", ".join(str(i) for i in answer), end="")
    print(">", end="")

if '__main__' == __name__:
    solution()