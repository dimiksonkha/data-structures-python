class Node:
    
    #Node Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    # set node data
    def set_data(self, data):
        self.data = data
    
    # return node data 
    def get_data(self):
        return self.data

    # set next node
    def set_next(self, next_node):
        self.next = next_node

    # return next node
    def get_next(self):
        return self.next

    #set previous node
    def set_prev(self, prev_node):
        self.prev = prev_node

    # return previous node
    def get_prev(self):
        return self.prev 
