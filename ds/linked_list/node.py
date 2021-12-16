class Node:
    
    #Node Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_prev(self):
        return self.prev 
