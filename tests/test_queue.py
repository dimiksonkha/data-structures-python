from ds.queue import Queue

def test_queue():
    
    queue = Queue()

    assert queue.is_empty() == True
    assert queue.size() == 0

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.is_empty() == False
    assert queue.size() == 3

    queue.dequeue()
    

    assert queue.size() == 2





