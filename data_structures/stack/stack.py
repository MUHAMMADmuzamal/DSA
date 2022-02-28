"""
    Stack
        A Stack is a collection of elements, with two principle operations:
            push, which adds to the collection, and pop, which removes the most
            recently added element
        Last in, first out data structure (LIFO): the most recently added
            object is the first to be removed
        Time Complexity:
            - Access: O(n)
            - Search: O(n)
            - Insert: O(1)
            - Remove: O(1)
"""

from collections import deque


class Stack:
    """Methods that perform various stack operations"""

    def __init__(self) -> None:
        """Initialize the stack"""
        self.stack = deque()

    def is_empty(self) -> bool:
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def push(self, item: any) -> None:
        """Push an item onto the stack"""
        self.stack.append(item)

    def pop(self) -> any:
        """Pop the last item off the stack and return it"""
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self) -> any:
        """Return the last element of the list"""
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self) -> int:
        """Return the size of the list"""
        return len(self.stack)


if __name__ == '__main__':
    # """ Test code."""
    s = Stack()
    for i in range(10):
        s.push(i)
    print(s.peek())
    print("----------")
    print(s.is_empty())
    print("---------")
    for i in range(s.size()):
        print(s.pop())
    print("----------")
    print(s.is_empty())
    print("---------")
