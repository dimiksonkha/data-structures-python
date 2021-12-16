from ds.linked_list.node import Node

def test_node():
    node_prev = Node(1)
    node = Node(2)
    node_next = Node(3)

    assert node.get_prev() == None
    assert node.get_next() == None
    assert node.get_data() == 2

    node.set_prev(node_prev)
    node.set_next(node_next)
    node.set_data(4)

    assert node.get_prev() == node_prev
    assert node.get_prev().get_data() == 1

    assert node.get_next() == node_next
    assert node.get_next().get_data() == 3

    assert node.get_data() == 4

    


    