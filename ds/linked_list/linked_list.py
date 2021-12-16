"""
Python implementaion of doubly linked list
"""
from typing import Counter
from ds.linked_list.node import Node


class LinkedList:
    
    # Linked list constructor 
    def __init__(self):
        self.head = None
        self.tail = None

    # retrun boolean if the list is empty or not 
    def is_empty(self):
        return self.head == None    

    # add item to the list
    def add(self, item):
        if self.is_empty():
            self.head = item
            self.tail = item
        else:
            temp = self.tail
            self.tail = item
            temp.next = item 
            item.prev = temp

    # remove the item from the list
    def remove(self, item):
        if item.next == None:
            item.prev.next = None
            temp = item.prev
            item.prev = None
            self.tail = temp

        else:
            item.prev.next = item.next
            item.next.prev = item.prev    
    
    # search an item in the list
    def search(self, item):
        found = False
        current = self.head
        
        while found != True:
            if item == current:
                found = True
            else:
                current = current.next
        
        return found                    

                    