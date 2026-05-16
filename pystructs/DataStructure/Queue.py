from pystructs.DataStructure.Node import Node

class Queue:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self):
        self.tail = None
        self.head = self.tail

    # Enqueue Method : Adds a node to the front of the Object
    def enqueue(self,data):
        new_node = Node.Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Dequeue Method : Removes a node from the rear of the Object
    def dequeue(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.head.data
            self.head = self.head.next
            return value
        
    # Peek Method : Views the data at the front of the Object
    def peek(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.head.data
            return value

    # Clear Method : Removes all nodes from the Object
    def clear(self):
        self.tail = None
        self.head = self.tail

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    # Len Method : Returns the total number of nodes in the Object
    def __len__(self):
        if self.head == None:
            return 0
        else:
            index = 0
            current = self.head
            while current != None:
                index += 1
                current = current.next
            return index

    # Iter Method : Iterates through each node in the Object by yielding values one by one
    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next

    # Contains Method : Checks if a specific value exists in the Object using the `in` keyword
    def __contains__(self, value):
        if self.head == None:
            return False
        else:
            current = self.head
            while current != None:
                if current.data == value:
                    return True
                current = current.next
            return False
        
    # Eq Method : Compares two Objects to determine if they are the same class and have identical nodes
    def __eq__(self, value):
        if not isinstance(value,Queue):
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
        return f"Queue({self.__str__()})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return bool(self.head)

    # Str Method : Displays all values within the Object
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
        