from ds.stack import Stack

def test_stack():
    
    stack = Stack()

    assert stack.is_empty() == True
    assert stack.size() == 0

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.is_empty() == False
    assert stack.size() == 3
    assert stack.peek() == 3

    stack.pop()

    assert stack.size() == 2
    assert stack.peek() == 2




