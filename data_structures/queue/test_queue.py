from .queue import Queue
q = Queue()
q.enqueue(1)
print(q.dequeue())
def test_enqueue():
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    assert q.dequeue() == 1