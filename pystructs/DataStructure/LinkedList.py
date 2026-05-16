# Import Node ของ LinkedList
from pystructs.DataStructure.Node import Node

class LinkedList:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # constructor 
    def __init__(self):
        self.head = None

    # Depth_First_Search Method (Private) : Used for traversing data using Depth First Search within the Object
    def _depth_first_search(self,value):
        if self.head == None:
            return False
        
        length = len(self) - 1

        current = self.head
        for index in range(length):
            if current.data == value:
                return True
            current = current.next

        return False
    
    # Breadth_First_Search Method (Private) : Used for traversing data using Depth First Search within the Object
    def _breadth_first_search(self,value):
        if self.head == None:
            return False
        
        length = len(self) - 1

        current = self.head
        for index in range(length):
            if current.data == value:
                return True
            current = current.next

        return False

    # Append Method : Adds an element to the end (tail) of the Object
    def append(self,data):
        new_node = Node.Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    # AppendLeft Method : Adds an element to the front (head) of the Object
    def appendleft(self,data):
        new_node = Node.Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert Method : Inserts data at the specified position and existing node at that position shifts to the right
    def insert(self,key,value):
        new_node = Node.Node(value)
        if key >= len(self):
            self.append(value)
        elif key == 0:
            self.prepend(value)
        else:
            current = self.head
            index = 0
            while index != key-1:
                current = current.next
                index += 1
            new_node.next = current.next
            current.next = new_node
            

    # Pop Method : Removes the last element from the Object and returns the removed value
    def pop(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        elif self.head.next == None:
            remove_node = self.head
            value = remove_node.data
            self.head = None
            return value
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            remove_node = current.next
            value = remove_node.data
            current.next = None
            return value
        
    # PopLeft Method : Removes the first element from the Object and returns the removed value
    def popleft(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.head.data
            self.head = self.head.next
            return value   
        
    # Remove Method : Removes the node at the specified index in the Object
    def remove(self,key):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        if key >= len(self):
            raise IndexError(self.IndexOutOfRange)
        if key == 0:
            self.head = self.head.next
        else:
            index = 0
            current = self.head
            while index != key-1:
                current = current.next
                index += 1
            current.next = current.next.next

    # Search Method : Finds the first occurrence of a value and returns the index of that node
    def find(self , data):
        if self.head == None:
            return None
        else:
            index = 0
            current = self.head
            while current != None:
                if current.data == data:
                    return index
                index += 1
                current = current.next
            return -1

    # Reverse Method : Reorders the nodes in the Object by reversing the order (back to front)
    def reverse(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            previous = None
            current = self.head
            while current != None:
                next = current.next
                current.next = previous
                previous = current
                current = next
            self.head = previous

    # Min Method : Find a minimum value in object and return
    def min(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)

        current = self.head
        min_value = current.data

        while current != None:
            if current.data < min_value:
                min_value = current.data
            current = current.next

        return min_value

    # Max Method : Find a maximum value in object and return
    def max(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)

        current = self.head
        max_value = current.data

        while current != None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

    # Clear Method : Removes all nodes from the Object
    def clear(self):
        self.head = None

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    # GetItem Method : Accesses a node value within the Object using a key via `[]`
    def __getitem__(self, key):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        if isinstance(key,slice):
            step = key.step if key.step != None else 1
            if step < 0:
                start = key.start if key.start != None else len(self) - 1
                stop = key.stop if key.stop != None else -1
            else:
                start = key.start if key.start != None else 0
                stop = key.stop if key.stop != None else len(self)
            
            value = LinkedList()
            for i in range(start,stop,step):
                value.append(self[i])
            return value
        else:
            if key < 0:
                key = len(self) + key
            count = 0
            current = self.head
            while count != key:
                current = current.next
                if current == None:
                    raise IndexError(self.IndexOutOfRange)
                count += 1
            return current.data
    
    # SetItem Method : Modifies a node value within the Object using a key via `[]`
    def __setitem__(self, key, value):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        if key >= len(self):
            raise IndexError(self.IndexOutOfRange)
        else:
            current = self.head
            index = 0
            while index != key:
                current = current.next
                index += 1
            current.data = value
        
    # Len Method : Returns the total number of nodes in the Object
    def __len__(self):
        if self.head == None:
            return 0
        else:
            index = 0
            current = self.head
            while current != None:
                current = current.next
                index += 1
            return index

    # Contains Method : Checks if a specific value exists in the Object using the `in` keyword
    def __contains__(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False

    # Iter Method : Iterates through each node in the Object by yielding values one by one
    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next 

    # Eq Method : Compares two Objects to determine if they are the same class and have identical nodes
    def __eq__(self, value):
        if not isinstance(value,LinkedList):
            return False
        elif len(self) != len(value):
            return False
        else:
            current = self.head
            check = value.head
            while current != None:
                if current.data != check.data:
                    return False
                current = current.next
                check = check.next
            return True
        
    # Repr Method : Displays the Object type when the `repr()` function is called
    def __repr__(self):
        return f"LinkedList({self.__str__()})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return bool(self.head)
            
    # Str Method : Displays all values within the Object when printed
    def __str__(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            current = self.head
            value = []
            while current != None:
                value.append(current.data)
                current = current.next
            return " → ".join(map(str,value)) + " → None"     
        