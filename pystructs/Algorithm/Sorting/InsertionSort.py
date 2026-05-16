
# Insertion Sort Function : Sort items in object with insertion sort algorithm

def insertion_sort(data):
    index = len(data)

    for i in range(1,index):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j = j - 1

        data[j+1] = key

    return data
