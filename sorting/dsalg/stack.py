from abc import ABC, abstractmethod

"""
Stack implementation
LIFO
"""


class Stack:

    @abstractmethod
    def push(self, element: int):
        pass

    @abstractmethod
    def pop(self) -> int:
        pass

    @abstractmethod
    def peek(self) -> int:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def full(self) -> bool:
        pass

    @abstractmethod
    def print_stack(self):
        pass


class StackImpl(Stack):

    def print_stack(self):
        for val in self.array:
            print(val, end=',')

    def __error_on_empty_stack__(self, op):
        if self.size == 0:
            raise Exception(f'[{op.upper()}] Stack is empty')

    def __init__(self, capacity: int):
        self.array = []
        self.size = 0
        self.capacity = capacity

    def push(self, element: int):
        if self.size == self.capacity:
            raise Exception("Stack is full")
        # add item to the top of the stack
        self.array.append(element)
        self.size += 1

    def pop(self) -> int:
        self.__error_on_empty_stack__('pop')
        popped = self.array[-1]
        self.array = self.array[0: -1]
        self.size -= 1
        return popped

    def peek(self) -> int:
        self.__error_on_empty_stack__('peek')
        return self.array[-1]

    def empty(self) -> bool:
        return self.size <= 0

    def full(self) -> bool:
        return self.size == len(self.array)


stack: Stack = StackImpl(capacity=5)
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(0)
stack.print_stack()
print('\npopped:', stack.pop())
print('peek:', stack.peek())
print('is_empty:', stack.empty())
print('is_full:', stack.full())

