"""
Python implementation of Heap data structure.
Heap is a complete binary tree
When any parent node data is greater than it's child node data then it is called Heap
The value of heap[1] is the root node
The value of heap[parent_index*2] is the left child
The value of heapd[parent_index*2+1] is the right child
Ex:
heap[2*2] is the left child of parent node at indext 2
heap[2*2+1] is the right child of parent node at indext 2

"""
def left(index):
  return 2*index

def right(index):
  return 2*index+1

def parent(index):
  return index/2  

# max heapify the given heap from the given index
def max_heapify(heap,heap_size,root_index):
  left_index = left(root_index)
  right_index = right(root_index)
  largest = None

  if left_index <= heap_size and heap[left_index] > heap[root_index]:
    largest = left_index
  else:
    largest = root_index

  if right_index <= heap_size and heap[right_index] > heap[largest]:
    largest = right_index

  if largest != root_index:
    t = heap[root_index]
    heap[root_index] = heap[largest]
    heap[largest] = t

  max_heapify(heap,heap_size,largest)

def build_max_heap(heap,heap_size):
  for i in range(heap_size/2,1,-1):
    max_heapify(heap,heap_size,i)


