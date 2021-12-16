from ds.linked_list.linked_list import LinkedList
from ds.linked_list.node import Node

def test_linked_list():
    
    linked_list = LinkedList()

    assert linked_list.is_empty() == True
    assert linked_list.head == None
    assert linked_list.tail == None
    
    node_a = Node(1)
    linked_list.add(node_a)
    assert linked_list.is_empty() == False
    assert linked_list.head == node_a
    assert linked_list.tail == node_a
    
    
    node_b = Node(2)
    linked_list.add(node_b)
    assert linked_list.head == node_a
    assert linked_list.tail == node_b
    assert node_a.next == node_b
    assert node_a.prev == None  
    
    node_c = Node(3)
    linked_list.add(node_c)
    assert linked_list.head == node_a
    assert linked_list.head.get_data() == 1
    
    assert node_b.prev == node_a
    assert node_b.next == node_c 

    assert linked_list.tail == node_c
    assert linked_list.tail.get_data() == 3
    assert node_c.next == None

    node_d = Node(66)
    linked_list.add(node_d)

    assert linked_list.search(node_c) == True

    linked_list.remove(node_c)
    assert linked_list.tail == node_d

    linked_list.remove(node_d)
    assert linked_list.tail == node_b  
    

    
    
    
