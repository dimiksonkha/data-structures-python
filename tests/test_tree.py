from ds.tree.tree import Tree
from ds.tree.node import Node

def test_tree():
    node_a = Node(2)
    tree = Tree()

    assert tree.get_root() == None

    tree.set_root(node_a)

    assert tree.get_root() == node_a

    node_b = Node(3)
    node_c = Node(4)

    node_a.add_left_child(node_b)
    node_a.add_right_child(node_c)

    assert type(node_a) == Node
    assert node_a.data == 2
    assert node_a.left == node_b
    assert node_a.right == node_c

    tree.pre_order(node_a)
    tree.post_order(node_a)
    tree.in_order(node_a)

