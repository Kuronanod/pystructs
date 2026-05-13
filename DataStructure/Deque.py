# Import Node ของ Deque
from Node import DequeNode

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

    # Append Method : เพิ่ม Node ด้านหลังสุดของ Object
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

    # AppendLeft Method : เพิ่ม Node ด้านหน้าสุดของ Object
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

    # Set_Head Method : แก้ข้อมูลของ Node ด้านหน้าสุดของ Object
    def set_head(self,data):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            self.head.data = data

    # Set_Tail Method : แก้ไข้อมูลของ Node ด้านหลังสุดของ Object
    def set_tail(self,data):
        if self.tail == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            self.tail.data = data

    # Peek Method : ดูข้อมูลของ Node ส่วนหลังสุดของ Object
    def peek(self):
        if self.tail == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            return self.tail.data
        
    # PeekLeft Method : ดูข้อมูลของ Node ส่วนหน้าสุดของ Object
    def peekleft(self):
        if self.head == None:
            raise IndexError(self.EmptyErrorMessage)
        else:
            return self.head.data

    # Pop Method : ลบ Node ด้านหลังสุดของ Object
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

    # PopLeft Method : ลบ Node ด้านหน้าสุดของ Object
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

    # Clear Method : ลบ Node ทั้งหมดของ Object
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

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
        
    # Len Method : หาจำนวน Node ทั้งหมดใน Object แล้ว Return ค่า 
    def __len__(self):
        return self.size
    
    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
    def __contains__(self, data):
        current = self.head
        while current != None:
            if current.data == data:
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

    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr()
    def __repr__(self):
        return f"Deque({self.__str__()})"
    
    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return bool(self.head)

    # Str Method : แสดงผลค่าใน Object ทั้งหมด
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
            