"""
Python stack implementation
"""

class Stack:
    
    # Constructor
    def __init__(self):
        self.items = []

    # Return if the stack is empty
    def is_empty(self):
        return self.items == []

    # Add new item to the top of the stack
    def push(self,item):
        self.items.append(item)

    # Remove the top item from the the stack
    def pop(self):
        self.items.pop()

    # Return the top item from the stack
    def peek(self):
        return self.items[-1]

    # Return the length of the stack
    def size(self):
        return len(self.items)
                    
           