
# Median Of Three Function : Choose pivot between first item , middle item , last item
def __median_of_three(data,low,high):

    middle = (low + high) // 2

    if data[low] > data[middle]:
        data[low] , data[middle] = data[middle] , data[low]
    if data[low] > data[high]:
        data[low] , data[high] = data[high] , data[low]
    if data[middle] > data[high]:
        data[middle] , data[high] = data[high] , data[middle]

    return data[middle]

# Quick Sort Function : Sort items in object with quick sort algorithm
def quick_sort(data):

    # Quick Sort In Place Function (Private) : Sort item in object with recursive partition
    def __quick_sort_in_place(low,high):
        if low < high:
            value = __partition(low,high)
            __quick_sort_in_place(low , value - 1)
            __quick_sort_in_place(value + 1 , high)

    # Partition Function (Private) : Sort a item in range of pivot on left and right partition
    def __partition(low,high):
        pivot = __median_of_three(data,low,high)
        
        for index in range(low,high+1):
            if data[index] == pivot:
                data[index] , data[high] = data[high] , data[index]
                break

        i = low - 1
        for j in range(low,high):
            if data[j] <= pivot:
                i += 1
                data[i] , data[j] = data[j] , data[i]

        data[i + 1] , data[high] = data[high] , data[i + 1]
        return i + 1

    __quick_sort_in_place(0 , len(data) - 1)
    
    return data
