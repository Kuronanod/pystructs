
class Heap():

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self,is_min = True):
        self.is_min = is_min
        self.heap = []

    # Class Method For Min Heap
    @classmethod
    def min_heap(cls):
        return cls(True)
    
    # Class Method For Max Heap
    @classmethod
    def max_heap(cls):
        return cls(False)
    
    # Heapify Up Method (Private) : Organizes the Object to maintain heap property after inserting data
    def _heapify_up(self,index):
        while index > 0:
            parent = (index - 1) // 2
            if self.is_min:
                if self.heap[index] >= self.heap[parent]:
                    break
            else:
                if self.heap[index] <= self.heap[parent]:
                    break
            self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
            index = parent

    # Heapify Down Method (Private) : Organizes the Object to maintain heap property after removing data
    def _heapify_down(self,index):
        size = len(self) - 1
        while True:
            left = (2 * index) + 1
            right = (2 * index) + 2
            value = index

            if self.is_min:
                if left <= size and self.heap[left] < self.heap[value]:
                    value = left
                if right <= size and self.heap[right] < self.heap[value]:
                    value = right
                if value == index:
                    break
            else:
                if left <= size and self.heap[left] > self.heap[value]:
                    value = left
                if right <= size and self.heap[right] > self.heap[value]:
                    value = right
                if value == index:
                    break

            self.heap[index] , self.heap[value] = self.heap[value] , self.heap[index]

            index = value

    # Push Method : Adds data to the Object
    def push(self,data):
        self.heap.append(data)
        self._heapify_up(len(self) - 1)

    # Peek Method : Returns the top value of the Object without removing it
    def peek(self):
        if not self.heap:
            raise IndexError(self.EmptyErrorMessage)
        return self.heap[0]
    
    # Max Method : Returns the maximum value in the Object
    def max(self):
        if self.is_min:
            return max(self.heap)
        else:
            return self.heap[0]
        
    # Min Method : Returns the minimum value in the Object
    def min(self):
        if self.is_min:
            return self.heap[0]
        else:
            return min(self.heap)

    # Pop Method : Removes and returns the top value of the Object
    def pop(self):
        if not self.heap:
            raise IndexError(self.EmptyErrorMessage)
        
        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]

        value = self.heap.pop()
        self._heapify_down(0)

        return value
    
    # Clear Method : Removes all data from the Object
    def clear(self):
        self.heap.clear()

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False
        
    # GetItem Method : Accesses data in the Object using a key via `[]`
    def __getitem__(self, key):
        if isinstance(key,slice):
            return self.heap[key]
        if key >= len(self):
            raise IndexError(self.IndexOutOfRange)
        return self.heap[key]

    # Len Method : Returns the total number of elements in the Object
    def __len__(self):
        return len(self.heap)
        
    # Iter Method : Iterates through each value in the Object by yielding values one by one
    def __iter__(self):
        return iter(self.heap)
    
    # Eq Method : Compares two Objects to determine if they are the same class and have identical values
    def __eq__(self, value):
        if not isinstance(value,Heap):
            return False
        return self.heap == value.heap and self.is_min == value.is_min
    
    # Contains Method : Checks if a specific value exists in the Object using the `in` keyword
    def __contains__(self, value):
        return value in self.heap
    
    # Repr Method : Displays the Object type when the `repr()` function is called
    def __repr__(self):
        return f"{self.__class__.__name__}({self.heap})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return bool(self.heap)
    
    # Str Method : Displays all values within the Object
    def __str__(self):
        if self.heap:
            return str(self.heap)
        else:
            raise IndexError(self.EmptyErrorMessage)