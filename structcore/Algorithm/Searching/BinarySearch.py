
# Binary Search Function : Search item in object with binary search algorithm

def binary_search(data,value):

    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        if data[middle] == value:
            return middle
        elif data[middle] < value:
            low = middle + 1
        else:
            high = middle - 1

    return -1
