"""
Python implementation of node for tree data structure

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left_child(self, child):
        self.left = child

    def add_right_child(self, child):
        self.right = child

        
        
