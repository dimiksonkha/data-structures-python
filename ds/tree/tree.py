from ds.tree.node import Node


class Tree:

    # Constructor
    def __init__(self):
        self.root = None

    # Set root node
    def set_root(self, node):
        self.root = node

    # Get root node
    def get_root(self):
        return self.root

    # pre order travarsel. root -> left -> right oder  
    def pre_order(self,node):
        print(node.data)

        if node.left != None:
            self.pre_order(node.left)

        if node.right!= None:    
            self.pre_order(node.right)

    # post order travarsel. left -> right oder -> root   
    def post_order(self,node):

        if node.left != None:
            self.post_order(node.left)

        if node.right!= None:    
            self.post_order(node.right) 

        print(node.data)

    # in order travarsel. left -> root -> right oder   
    def in_order(self,node):

        if node.left != None:
            self.in_order(node.left)

        print(node.data)      

        if node.right!= None:    
            self.in_order(node.right) 

                     
        


    