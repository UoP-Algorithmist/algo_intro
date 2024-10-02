from abc import abstractmethod
from typing import Any

"""
Queue implementation
LIFO
"""


class Queue:

    @abstractmethod
    def enqueue(self, element):
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def first(self) -> bool:
        pass

    @abstractmethod
    def printall(self):
        pass


class QueueImpl(Queue):

    def printall(self):
        print(self.queue)

    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.size = 0

    def enqueue(self, element):
        if self.is_full():
            raise Exception(f"[ENQUEUE] queue is full")
        self.queue.append(element)
        self.size += 1

    def dequeue(self):
        if self.size <= 0:
            raise Exception(f"[DEQUEUE] queue is empty")
        dequeued = self.queue[0]
        self.queue = self.queue[1:]
        self.size -= 1
        return dequeued

    def is_full(self) -> bool:
        return self.capacity == self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self) -> bool:
        return self.queue[0]


# Test
queue: Queue = QueueImpl(4)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(9)
print('first: ', queue.first())
queue.printall()
print('dequeued: ', queue.dequeue())
queue.printall()
