from DataStructure.Heap import Heap

def heap_sort(data):

    heap = Heap.max_heap()
    for value in data:
        heap.push(value)

    result = []
    while heap:
        result.append(heap.pop())

    return result[::-1]

input = [34,12,8,34,674,12,987,32,756,132,0,32,54,21,43,54]
print(heap_sort(input))