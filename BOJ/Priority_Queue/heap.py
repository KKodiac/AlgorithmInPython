# How to implement max/min heap in Python
import heapq
# Max Heap
def max_heap():
    heap = []
    heapq.heapify(heap)

    heapq.heappush(heap, -1 * 10)
    heapq.heappush(heap, -1 * 30)
    heapq.heappush(heap, -1 * 20)
    heapq.heappush(heap, -1 * 400)

    print("Head value of heap : " + str(-1 * heap[0]))

    print("Heap elements : ")
    for i in heap:
        print(-1 * i, end=' ')
    print('\n')

    element = heapq.heappop(heap)

    print("Heap Elements : ")
    for i in heap:
        print(-1 * i, end = ' ')


# Min heap
def min_heap():
    heap = []
    heapq.heapify(heap)

    heapq.heappush(heap, 10)
    heapq.heappush(heap, 30)
    heapq.heappush(heap, 20)
    heapq.heappush(heap, 400)

    print("Head value of heap : " + str(-1 * heap[0]))

    print("Heap elements : ")
    for i in heap:
        print(i, end=' ')
    print('\n')

    element = heapq.heappop(heap)

    print("Heap Elements : ")
    for i in heap:
        print(i, end=' ')

if '__main__' == __name__:
    max_heap()
    print('\n')
    print('\n')
    min_heap()