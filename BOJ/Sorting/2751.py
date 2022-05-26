# BOJ 2751번 문제: 수 정렬하기 2
import sys
import heapq
def solution():
    N = int(sys.stdin.readline())
    heap = list()
    heapq.heapify(heap)
    for i in range(N):
        num = int(sys.stdin.readline())
        heapq.heappush(heap, num)

    for j in range(N):
        answer = heapq.heappop(heap)
        sys.stdout.write(answer)


if '__main__' == __name__:
    solution()


