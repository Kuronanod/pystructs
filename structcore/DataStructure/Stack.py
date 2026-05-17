from pystructs.DataStructure.Node import Node

class Stack:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"
    
    # Constructor
    def __init__(self):
        self.top = None

    # Push Method : Adds a new node to the top of the Object
    def push(self,data):
        new_node = Node.Node(data)
        new_node.next = self.top
        self.top = new_node

    # Update Method : Modifies the data of the top node in the Object
    def update(self,data):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            self.top.data = data

    # Peek Method : Accesses and returns the data of the top node in the Object
    def peek(self):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            return self.top.data

    # Pop Method : Removes the top node from the Object
    def pop(self):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.top.data
            self.top = self.top.next
            return value
    
    # Clear Method : Removes all nodes from the Object
    def clear(self):
        self.top = None
        
    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    # Len Method : Returns the total number of nodes in the Object
    def __len__(self):
        if self.top == None:
            return 0
        else:
            index = 0
            current = self.top
            while current != None:
                index += 1
                current = current.next
            return index
        
    # Iter Method : Iterates through each node in the Object by yielding values one by one
    def __iter__(self):
        current = self.top
        while current != None:
            yield current.data
            current = current.next

    # Contains Method : Checks if a specific value exists in the Object using the `in` keyword
    def __contains__(self, value):
        if self.top == None:
            return False
        else:
            current = self.top
            while current != None:
                if current.data == value:
                    return True
                current = current.next
            return False
        
    # Eq Method : Compares two Objects to determine if they are the same class and have identical nodes
    def __eq__(self, value):
        if not isinstance(value,Stack):
            return False
        elif len(self) != len(value):
            return False
        else:
            current = self.top
            check = value.top
            while current != None:
                if current.data != check.data:
                    return False
                current = current.next
                check = check.next
            return True
        
    # Repr Method : Displays the Object type when the `repr()` function is called
    def __repr__(self):
        return f"Stack({self.__str__()})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return bool(self.top)

    # Str Method : Displays all values within the Object
    def __str__(self):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            current = self.top
            value = []
            while current != None:
                value.append(current.data)
                current = current.next
            return  " → ".join(map(str,value)) + " → None"
