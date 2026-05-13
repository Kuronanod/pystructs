from Node import Node

class Queue:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self):
        self.tail = None
        self.head = self.tail

    # Enqueue Method : เพิ่ม Node เข้าด้านหน้าสุดของ Object
    def enqueue(self,data):
        new_node = Node.Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Dequeue Method : ลบ Node ด้านหลังสุดของ Object
    def dequeue(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.head.data
            self.head = self.head.next
            return value
        
    # Peek Method : ดูข้อมูลที่อยู่ด้านหน้าสุดของ Object
    def peek(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.head.data
            return value

    # Clear Method : ลบ Node ทั้งหมดใน object
    def clear(self):
        self.tail = None
        self.head = self.tail

    # IsEmpty Method : ตรวจสอบว่า Object นี้เป็นค่าว่างไหม
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    # GetItem Method : เข้าถึงค่าใน Node ภายใน Object โดยใช้ Key ผ่าน []
    def __getitem__(self, key):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        elif isinstance(key,slice):
            step = key.step if key.step != None else 1
            if step < 0:
                start = key.start if key.start != None else len(self) - 1
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
                if current == None:
                    raise IndexError(self.IndexOutOfRange)
                current = current.next
                count += 1
            return current.data

    # Len Method : หาจำนวน Node ทั้งหมดใน Object แล้ว Return ค่า 
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

    # Iter Method : เข้าถึง Node ใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next

    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
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
        
    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและ Node ใน Object เหมือนกันไหม
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
        
    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr()
    def __repr__(self):
        return f"Queue({self.__str__()})"
    
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