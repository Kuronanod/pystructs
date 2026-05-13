from Node import BSTNode
from Deque import Deque

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

    # Is Equal Method (Private) : ตรวจสอบว่า Object ทั้งสองนั้นเหมือนกันไหมทั้งในเชิงข้อมูลและโครงสร้าง
    def _is_equal(self,object1,object2):
        if object1 == None and object2 == None:
            return True
        if object1 == None or object2 == None:
            return False
        
        return (object1.data == object2.data and self._is_equal(object1.left , object2.left) and self._is_equal(object1.right , object2.right))

    # Inorder Asc Helper Method (Private) : ช่วยเก็บข้อมูลใน Object โดยเรียงข้อมูลจากน้อยไปมาก
    def _inorder_asc_helper(self,node,result):
        if node == None:
            return
        self._inorder_asc_helper(node.left,result)
        result.append(node.data)
        self._inorder_asc_helper(node.right,result)

    # Inorder desc Helper Method (Private) : ช่วยเก็บข้อมูลใน Object โดยเรียงข้อมูลจากมากไปน้อย
    def _inorder_desc_helper(self,node,result):
        if node == None:
            return
        self._inorder_desc_helper(node.right,result)
        result.append(node.data)
        self._inorder_desc_helper(node.left,result)

    # Depth_First_Search_Recursive Method (Private) : ช่วยเรียงข้อมูลแบบ DepthFirstSearch สำหรับ Object
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

    # Depth_First_Search Method (Private) : เรียงข้อมูลแบบ DepthFirstSearch สำหรับ Object
    def _depth_first_search(self,value,order = "inorder"):    
        return self._depth_first_search_recursive(self.root , value , order)
    
    # Breadth_First_Search Method (Private) : เรียงข้อมูลแบบ BreadthFirstSearch สำหรับ Object
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

    # Insert Method : เพิ่ม Node ที่ต้องการเข้าไปใน Object
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
                
    # Search Method : ค้นหาข้อมูลที่ต้องการใน Object
    def search(self,data):
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

    # Inorder Asc Method : Return ค่าใน Object จากน้อยไปมาก
    def inorder_asc(self):
        value = []
        self._inorder_asc_helper(self.root,value)
        return value

    # Inorder Desc Method : Return ค่าใน Object จากมากไปน้อย
    def inorder_desc(self):
        value = []
        self._inorder_desc_helper(self.root,value)
        return value
    
    # Min Method : Return ค่าที่น้อยที่สุดใน Object
    def min(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        current = self.root
        while current.left != None:
            current = current.left
        return current.data

    # Max Method : Return ค่าที่มากที่สุดใน Object
    def max(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        current = self.root
        while current.right != None:
            current = current.right
        return current.data
    
    # Peek Method : ดู Node บนสุดของ Object (Root) แล้ว Return ค่า
    def peek(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        return self.root.data

    # Delete Method : ลบ Node ที่ต้องการใน Object
    def delete(self,data):
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

    # Clear Method : ลบ Node ทั้งหมดใน Object
    def clear(self):
        self.root = None
        self.size = 0

    # IsEmpty Method : ตรวจสอบว่า Object นี้เป็นค่าว่างไหม
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
        
    # Len Method : หาจำนวน Node ทั้งหมดใน Object แล้ว Return ค่า
    def __len__(self):
        return self.size
    
    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
    def __contains__(self, value):
        if self.root == None:
            return False
        return bool(self.search(value))
    
    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและค่าใน Object เหมือนกันไหม
    def __eq__(self, object):
        if not isinstance(object,BinarySearchTree):
            return False
        return self._is_equal(self.root , object.root)
    
    # Iter Method : เข้าถึงข้อมูลใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        return iter(self.inorder_asc())

    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return self.root is not None
    
    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr()
    def __repr__(self):
        return f"Binary Search Tree({self.__str__()})"

    # Str Method : แสดงผลค่าใน Object ทั้งหมด
    def __str__(self):
        if self.root == None:
            raise IndexError(self.EmptyErrorMessage)
        value = []
        self._inorder_asc_helper(self.root,value)
        return str(value)