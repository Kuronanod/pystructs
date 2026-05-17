# Import Node For Binary Search Tree 
from structcore.DataStructure.Node import BSTNode
from structcore.DataStructure.Deque import Deque

class BinarySearchTree():
    
    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"
    DuplicatedErrorMessage = "This Value Is Already Exist"

    # Constructor
    def __init__(self):
        self.root = None
        self.size = 0

    # Is Equal Method (Private) : Checks whether two Objects are identical in both data and structure
    def _is_equal(self,object1,object2):
        if object1 == None and object2 == None:
            return True
        if object1 == None or object2 == None:
            return False
        
        return (object1.data == object2.data and self._is_equal(object1.left , object2.left) and self._is_equal(object1.right , object2.right))

    # Inorder Asc Helper Method (Private) : Helper method to collect data in ascending order
    def _inorder_asc_helper(self,node,result):
        if node == None:
            return
        self._inorder_asc_helper(node.left,result)
        result.append(node.data)
        self._inorder_asc_helper(node.right,result)

    # Inorder desc Helper Method (Private) : Helper method to collect data in descending order
    def _inorder_desc_helper(self,node,result):
        if node == None:
            return
        self._inorder_desc_helper(node.right,result)
        result.append(node.data)
        self._inorder_desc_helper(node.left,result)

    # Depth_First_Search_Recursive Method (Private) : Helper method for Depth First Search traversal
    def _depth_first_search_recursive(self,node,value,order):
        
        if node == None:
            return False
        
        if order == "preorder":
            if node.data == value:
                return True
            return (self._depth_first_search_recursive(node.left , value , order)) or (self._depth_first_search_recursive(node.right , value , order))
        elif order == "inorder":
            if self._depth_first_search_recursive(node.left , value , order):
                return True
            if node.data == value:
                return True
            return self._depth_first_search_recursive(node.right , value , order)
        elif order == "postorder":
            if self._depth_first_search_recursive(node.left , value , order):
                return True
            if self._depth_first_search_recursive(node.right , value , order):
                return True
            return node.data == value
        
        return False

    # Depth_First_Search Method (Private) : Performs Depth First Search traversal on the Object
    def _depth_first_search(self,value,order = "inorder"):    
        return self._depth_first_search_recursive(self.root , value , order)
    
    # Breadth_First_Search Method (Private) : Performs Breadth First Search traversal on the Object
    def _breadth_first_search(self,value):
        
        if self.root == None:
            return False
        
        deque = Deque()
        deque.append(self.root)
        
        while not deque.isEmpty():
            node = deque.popleft()

            if node.data == value:
                return True
            
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

        return False

    # Insert Method : Adds a node to the Object
    def insert(self,data):
        new_node = BSTNode(data)
        if self.root == None:
            self.root = new_node
            self.size += 1
        else:
            current = self.root
            while True:
                if current.data < data:
                    if current.right == None:
                        current.right = new_node
                        self.size += 1
                        break
                    current = current.right
                elif current.data > data:
                    if current.left == None:
                        current.left = new_node
                        self.size += 1
                        break
                    current = current.left
                else:
                    raise IndexError(self.DuplicatedErrorMessage)
                
    # Find Method : Find a specific value within the Object
    def find(self,data):
        current = self.root
        while True:
            if current == None:
                return False
            elif current.data == data:
                return current
            else:
                if data < current.data:
                    current = current.left
                elif data > current.data:
                    current = current.right

    # Inorder Asc Method : Returns values in ascending order
    def inorder_asc(self):
        value = []
        self._inorder_asc_helper(self.root,value)
        return value

    # Inorder Desc Method : Returns values in descending order
    def inorder_desc(self):
        value = []
        self._inorder_desc_helper(self.root,value)
        return value
    
    # Min Method : Returns the smallest value in the Object
    def min(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        current = self.root
        while current.left != None:
            current = current.left
        return current.data

    # Max Method : Returns the largest value in the Object
    def max(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        current = self.root
        while current.right != None:
            current = current.right
        return current.data
    
    # Peek Method : Views the top node (Root) and returns its value
    def peek(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        return self.root.data

    # Remove Method : Removes a specified node from the Object
    def remove(self,data):
        current = self.root
        parent = None
        while True:
            if current == None:
                return False
            elif current.data == data:
                if current.left == None and current.right == None:
                    if parent == None:
                        self.root = None
                        self.size -= 1
                    elif parent.left == current:
                        parent.left = None
                        self.size -= 1
                    else:
                        parent.right = None
                        self.size -= 1
                    return True
                elif current.left == None:
                    if parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    self.size -= 1
                    return True
                elif current.right == None:
                    if parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    self.size -= 1
                    return True
                else:
                    successor_parent = current
                    successor = current.right
                    while True:
                        if successor.left == None:
                            break
                        successor_parent = successor
                        successor = successor.left
                    current.data = successor.data
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                    self.size -= 1
                    return True
            else:
                parent = current
                if data < current.data:
                    current = current.left
                elif data > current.data:
                    current = current.right

    # Clear Method : Removes all nodes from the Object
    def clear(self):
        self.root = None
        self.size = 0

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
        
    # Len Method : Returns the total number of nodes in the Object
    def __len__(self):
        return self.size
    
    # Contains Method : Checks if a specific value exists in the Object using the `in` keyword
    def __contains__(self, value):
        if self.root == None:
            return False
        return bool(self.find(value))
    
    # Eq Method : Compares two Objects to determine if they are the same class and have identical values
    def __eq__(self, object):
        if not isinstance(object,BinarySearchTree):
            return False
        return self._is_equal(self.root , object.root)
    
    # Iter Method : Iterates through each value in the Object by yielding values one by one
    def __iter__(self):
        return iter(self.inorder_asc())
    
    # Repr Method : Displays the Object type when the `repr()` function is called
    def __repr__(self):
        return f"Binary Search Tree({self.__str__()})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return self.root is not None

    # Str Method : Displays all values within the Object
    def __str__(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        value = []
        self._inorder_asc_helper(self.root,value)
        return str(value)