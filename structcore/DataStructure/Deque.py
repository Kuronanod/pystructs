# Import Node ของ Deque
from pystructs.DataStructure.Node import DequeNode

# class (Deque)
class Deque:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Append Method : Adds a node to the rear (tail) of the Object
    def append(self,data):
        new_node = DequeNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.size += 1

    # AppendLeft Method : Adds a node to the front (head) of the Object
    def appendleft(self,data):
        new_node = DequeNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    # Set_Head Method : Modifies the data of the node at the front of the Object
    def set_head(self,data):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            self.head.data = data

    # Set_Tail Method : Modifies the data of the node at the rear of the Object
    def set_tail(self,data):
        if self.tail == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            self.tail.data = data

    # Peek Method : Views the data of the node at the rear of the Object
    def peek(self):
        if self.tail == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            return self.tail.data
        
    # PeekLeft Method : Views the data of the node at the front of the Object
    def peekleft(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            return self.head.data

    # Pop Method : Removes the node from the rear of the Object
    def pop(self):
        if self.tail == None:
            raise IndexError(self.EmptyErrorMessage)
        
        previous = self.tail.previous
        value = self.tail.data

        if previous:
            previous.next = None
            self.tail = previous
            self.size -= 1
        else:
            self.head = None
            self.tail = None
            self.size -= 1

        return value

    # PopLeft Method : Removes the node from the front of the Object
    def popleft(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        
        next = self.head.next
        value = self.head.data

        if next:
            next.previous = None
            self.head = next
            self.size -= 1
        else:
            self.head = None
            self.tail = None
            self.size -= 1

    # Clear Method : Removes all nodes from the Object
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    # GetItem Method : Accesses a node's value within the Object using a key via `[]`
    def __getitem__(self, key):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        elif isinstance(key,slice):
            step = key.step if key.step != None else 1
            if step < 0:
                start = key.start if key.start != None else len(self) -1
                stop = key.stop if key.stop != None else -1
            else:
                start = key.start if key.start != None else 0
                stop = key.stop if key.stop != None else len(self)
            value = []
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
                    raise IndexError(self.EmptyErrorMessage)
                count += 1
            return current.data
        
    # Len Method : Returns the total number of nodes in the Object
    def __len__(self):
        return self.size
    
    # Contains Method : Checks if a specific value exists in the Object using the `in` keyword
    def __contains__(self, data):
        current = self.head
        while current != None:
            if current.data == data:
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
        if not isinstance(value,Deque):
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
        return f"Deque({self.__str__()})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return bool(self.head)

    # Str Method : Displays all values within the Object
    def __str__(self):
        current =  self.head
        value = []
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            while(current != None):
                value.append(current.data)
                current = current.next
            return " → ".join(map(str,value))
            