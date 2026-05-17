
# Selection Sort Function : Sort items in object with selection sort algorithm

def selection_sort(data):
    index = len(data)

    for i in range(index):
        min_index = i
        for j in range(i+1,index):
            if data[j] < data[min_index]:
                min_index = j
        data[i] , data[min_index] = data[min_index] , data[i]
    
    return data
