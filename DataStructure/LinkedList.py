# Import Node ของ LinkedList
from Node import Node

class LinkedList:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # constructor 
    def __init__(self):
        self.head = None

    # Depth_First_Search Method (Private) : เรียงข้อมูลแบบ DepthFirstSearch สำหรับ Object
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
    
    # Breadth_First_Search Method (Private) : เรียงข้อมูลแบบ BreadthFirstSearch สำหรับ Object
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

    # Append Method : เพิ่มข้อมูลด้านหลังสุดของ Object
    def append(self,data):

        new_node = Node.Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    # AppendLeft Method : เพิ่มข้อมูลด้านหน้าสุดของ Object
    def appendleft(self,data):

        new_node = Node.Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert Method : เพิ่มข้อมูลแทรกตามต่ำแหน่งที่ต้องการแล้วขยับ Node เก่าที่โดนแทรกไปต่อท้าย Node ที่เพิ่มมาใหม่
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
            

    # Pop Method : ลบข้อมูลด้านท้ายสุดแล้ว Return ค่าที่ลบ
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
        
    # PopLeft Method : ลบข้อมูลด้านหน้าสุดแล้ว Return ค่าที่ลบ
    def popleft(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.head.data
            self.head = self.head.next
            return value   
        
    # Remove Method : ลบข้อมูลตามต่ำแหน่งของ Node ที่ต้องการใน Object
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

    # Clear Method : ลบ Node ทั้งหมดใน Object
    def clear(self):
        self.head = None

    # Search Method : หาค่า data ตัวแรกที่เจอและ return เป็นต่ำแหน่งของ node ของค่านั้น
    def Search(self , data):
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

    # Reverse Method : ทำการเรียง Node ใน Object ใหม่โดยเรียงจากหลังไปหน้า
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
        
    # GetItem Method : เข้าถึงค่าใน Node ภายใน Object โดยใช้ Key ผ่าน []
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
    
    # SetItem Method : แก้ไขค่าใน Node ภายใน Object โดยใช้ key ผ่าน []
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
        
    # Len Method : หาจำนวน Node ที่มีทั้งหมดใน Object แล้ว Return ค่า 
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

    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
    def __contains__(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False

    # Iter Method : เข้าถึง Node ใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next 

    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและ Node ใน Object เหมือนกันไหม
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
        
    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr
    def __repr__(self):
        return f"LinkedList({self.__str__()})"
    
    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return bool(self.head)
            
    # Str Method : แสดงผลค่าใน Object ทั้งหมด
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
        