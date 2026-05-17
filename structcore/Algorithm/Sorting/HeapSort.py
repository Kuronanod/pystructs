from pystructs.DataStructure.Heap import Heap

# Heap Sort Function : Sort items in object with heap sort algorithm

def heap_sort(data):

    heap = Heap.max_heap()
    for value in data:
        heap.push(value)

    result = []
    while heap:
        result.append(heap.pop())

    return result[::-1]
