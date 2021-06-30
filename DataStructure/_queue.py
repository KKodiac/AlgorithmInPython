"""
    ADT for Linked List in Python
    dequeue : Removes an element from the front of the queue
    enqueue : Adds an element to the rear of the queue
    first   : Examines the element at the front of the queue
    isEmpty : Determines whether the queue is empty
    size    : Determines the number of elements in the queue
    toString: Returns a string representation of the queue
"""

class Queue:
    def __init__(self):
        self.queue = list()

    def dequeue(self) -> int:
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return -1

    def enqueue(self, value : int):
        self.queue.append(value)
    
    def first(self) -> int:
        return self.queue[0]

    def isEmpty(self) -> bool:
        return not len(self.queue) > 0
    
    def size(self) -> int:
        return len(self.queue)

    def toString(self) -> str:
        return "> ".join(str(i) for i in self.queue)

if __name__ == '__main__':
    q = Queue()
    assert q.dequeue() == -1
    q.enqueue(1)
    assert q.first() == 1
    q.dequeue()
    for i in range(1,10):
        q.enqueue(i)
    assert q.toString() == "1> 2> 3> 4> 5> 6> 7> 8> 9"