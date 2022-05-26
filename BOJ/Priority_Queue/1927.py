# BOJ 1927번 문제: 최소 힙
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
            print(element)
        else:
            heapq.heappush(heap, x)


if '__main__' == __name__:
    solution()
