# BOJ 11279번 문제: 최대 힙
import heapq
import sys


def solution():
    heap = list()
    heapq.heapify(heap)

    N = int(sys.stdin.readline())
    for i in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            if len(heap) == 0:
                element = 0
            else:
                element = heapq.heappop(heap)
            print(element * -1)
        else:
            heapq.heappush(heap, -1 * x)


if '__main__' == __name__:
    solution()
    