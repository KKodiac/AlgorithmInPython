# BOJ 11286 절댓값 힙
import heapq
import sys
def solution():
    n = int(input())
    heap = list()
    heapq.heapify(heap)
    for _ in range(n):
        x = int(sys.stdin.readline().rstrip())
        if x == 0:
            if len(heap) == 0:
                print(0)
            else:
                abs_x = heapq.heappop(heap)
                print(abs_x[1])
        else:
            heapq.heappush(heap, (abs(x), x))

if '__main__' == __name__:
    solution()