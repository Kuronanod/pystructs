from Node import Node

class Stack:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"
    
    # Constructor
    def __init__(self):
        self.top = None

    # Push Method : เพิ่ม Node ใหม่เข้าไปในด้านบนสุดของ Object
    def push(self,data):
        new_node = Node.Node(data)
        new_node.next = self.top
        self.top = new_node

    # Update Method : แก้ไขข้อมูลของ Node ด้านบนสุดของ Object
    def update(self,data):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            self.top.data = data

    # Peek Method : เข้าถึงข้อมูลของ Node ด้านบนสุดของ Object แล้ว Return ค่า
    def peek(self):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            return self.top.data

    # Pop Method : ลบ Node ด้านบนสุดของ Object
    def pop(self):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            value = self.top.data
            self.top = self.top.next
            return value
    
    # Clear Method : ลบ Node ทั้งหมดใน Object
    def clear(self):
        self.top = None
        
    # IsEmpty Method : ตรวจสอบว่า Object นี้เป็นค่าว่างไหม
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    # GetItem Method : เข้าถึงค่าใน Node ภายใน Object โดยใช้ Key ผ่าน []
    def __getitem__(self, key):
        if self.top == None:
            raise IndexError(self.EmptyErrorMessage)
        if isinstance(key,slice):
            step = key.step if key.step != None else 1
            if step < 0:
                start = key.start if key.start != None else len(self) - 1
                stop = key.stop if key.stop != None else -1
            else:
                start = key.start if key.start != None else 0
                stop = key.stop if key.stop != None else len(self)
            value = Stack()
            for i in range(start,stop,step):
                value.push(self[i])
            return value
        else:
            if key < 0:
                key = len(self) + key
            count = 0
            current = self.top
            while count != key:
                current = current.next
                if current == None:
                    raise IndexError(self.IndexOutOfRange)
                count += 1
            return current.data
        
    # Len Method : หาจำนวน Node ทั้งหมดใน Object แล้ว Return ค่า 
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
        
    # Iter Method : เข้าถึง Node ใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        current = self.top
        while current != None:
            yield current.data
            current = current.next

    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
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
        
    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและ Node ใน Object เหมือนกันไหม
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
        
    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr()
    def __repr__(self):
        return f"Stack({self.__str__()})"
    
    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return bool(self.top)

    # Str Method : แสดงผลค่าใน Object ทั้งหมด
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