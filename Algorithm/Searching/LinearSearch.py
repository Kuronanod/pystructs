
def linear_search(data,value):

    index = 0

    while index != len(data):
        if data[index] == value:
            return index
        else:
            index += 1

    return -1
