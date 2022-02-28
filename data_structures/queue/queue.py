"""
    Queue
        A Queue is a collection of elements, supporting two principle
            operations: enqueue, which inserts an element into the queue,
            and dequeue, which removes an element from the queue
        First in, first out data structure (FIFO): the oldest added
            object is the first to be removed
        Time Complexity:
            - Access: O(n)
            - Search: O(n)
            - Insert: O(1)
            - Remove: O(1)
"""

from collections import deque


class Queue:
    """Methods that perform various Queue operations"""

    def __init__(self) -> None:
        """Initialize the queue"""
        self.queue = deque()

    def is_empty(self) -> bool:
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def enqueue(self, item: any) -> None:
        """Add an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self) -> any:
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        return self.queue.popleft()

    def size(self) -> int:
        """Return the size of the list"""
        return len(self.queue)


if __name__ == '__main__':
    # """Test code """
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print(q.is_empty())
    for i in range(q.size()):
        print(q.dequeue())
    print(q.is_empty())