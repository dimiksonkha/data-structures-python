"""
Python Queue implementation
"""

class Queue:
    
    # Constructor
    def __init__(self):
        self.items = []

    # Return if the queue is empty
    def is_empty(self):
        return self.items == []

    # Add new item to the rear of the queue
    def enqueue(self,item):
        self.items.append(item)

    # Remove the front item from the the queue
    def dequeue(self):
        del(self.items[0])

    # Return the length of the queue
    def size(self):
        return len(self.items)
                    
           