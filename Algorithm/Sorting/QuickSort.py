
def median_of_three(data,low,high):

    middle = (low + high) // 2

    if data[low] > data[middle]:
        data[low] , data[middle] = data[middle] , data[low]
    if data[low] > data[high]:
        data[low] , data[high] = data[high] , data[low]
    if data[middle] > data[high]:
        data[middle] , data[high] = data[high] , data[middle]

    return data[middle]

def quick_sort(data):

    def _quick_sort_in_place(low,high):
        if low < high:
            value = partition(low,high)
            _quick_sort_in_place(low , value - 1)
            _quick_sort_in_place(value + 1 , high)

    def partition(low,high):
        pivot = median_of_three(data,low,high)
        
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

    _quick_sort_in_place(0 , len(data) - 1)
    
    return data
