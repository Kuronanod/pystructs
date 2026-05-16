
# Bubble_Sort Function : Sort items in object with bubble sort algorithm

def bubble_sort(data):
    index = len(data)

    for i in range(index):
        swap = False
        for j in range(index - i - 1 ):
            if data[j] > data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
                swap = True
        if not swap == True:
            break

    return data
