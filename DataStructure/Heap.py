
class Heap():

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self,is_min = True):
        self.is_min = is_min
        self.heap = []

    # Class Method สำหรับ Min Heap
    @classmethod
    def min_heap(cls):
        return cls(True)
    
    # Class Method สำหรับ Max Heap
    @classmethod
    def max_heap(cls):
        return cls(False)
    
    # Heapify Up Method (Private) : จัดระเบียบของ Object ให้เป็นไปตามกฎของ Heap ตอนเพิ่มข้อมูลเข้ามา
    def _heapify_up(self,index):
        while index > 0:
            parent = (index - 1) // 2
            if self.is_min:
                if self.heap[index] >= self.heap[parent]:
                    break
            else:
                if self.heap[index] <= self.heap[parent]:
                    break
            self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
            index = parent

    # Heapify Down Method (Private) : ใช้สำหรับจัดระเบียบของ Object ให้เป็นไปตามกฎของ Heap ตอนลบข้อมูลออกไป
    def _heapify_down(self,index):
        size = len(self) - 1
        while True:
            left = (2 * index) + 1
            right = (2 * index) + 2
            value = index

            if self.is_min:
                if left <= size and self.heap[left] < self.heap[value]:
                    value = left
                if right <= size and self.heap[right] < self.heap[value]:
                    value = right
                if value == index:
                    break
            else:
                if left <= size and self.heap[left] > self.heap[value]:
                    value = left
                if right <= size and self.heap[right] > self.heap[value]:
                    value = right
                if value == index:
                    break

            self.heap[index] , self.heap[value] = self.heap[value] , self.heap[index]

            index = value

    # Push Method : เพิ่มข้อมูลลงไปใน Object
    def push(self,data):
        self.heap.append(data)
        self._heapify_up(len(self) - 1)

    # Peek Method : ดูค่าบนสุดของ Object แล้ว Return ค่า
    def peek(self):
        if not self.heap:
            raise IndexError(self.EmptyErrorMessage)
        return self.heap[0]
    
    # Get Max Method : ดูค่าที่มากสุดของ Object แล้ว Return ค่า
    def get_max(self):
        if self.is_min:
            return max(self.heap)
        else:
            return self.heap[0]
        
    # Get Min Method : ดูค่าที่น้อยสุดของ Object แล้ว Return ค่า
    def get_min(self):
        if self.is_min:
            return self.heap[0]
        else:
            return min(self.heap)

    # Pop Method : ลบค่าข้อมูลที่อยู่ท้ายสุดใน Object
    def pop(self):
        if not self.heap:
            raise IndexError(self.EmptyErrorMessage)
        
        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]

        value = self.heap.pop()
        self._heapify_down(0)

        return value
    
    # Clear Method : ลบข้อมูลทั้งหมดใน Object
    def clear(self):
        self.heap.clear()

    # IsEmpty Method : ตรวจสอบว่า Object นี้เป็นค่าว่างไหม
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False
        
    # GetItem Method : ใช้สำหรับการเข้าถึงข้อมูลใน Object โดยใช้ Key ผ่าน []
    def __getitem__(self, key):
        if isinstance(key,slice):
            return self.heap[key]
        if key >= len(self):
            raise IndexError(self.IndexOutOfRange)
        return self.heap[key]

    # Len Method : หาจำนวนข้อมูลทั้งหมดใน Object แล้ว Return ค่า
    def __len__(self):
        return len(self.heap)
    
    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr()
    def __repr__(self):
        return f"{self.__class__.__name__}({self.heap})"
        
    # Iter Method : เข้าถึงข้อมูลใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        return iter(self.heap)
    
    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและค่าใน Object เหมือนกันไหม
    def __eq__(self, value):
        if not isinstance(value,Heap):
            return False
        return self.heap == value.heap and self.is_min == value.is_min
    
    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
    def __contains__(self, value):
        return value in self.heap
    
    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return bool(self.heap)
    
    # Str Method : แสดงผลค่าใน Object ทั้งหมด
    def __str__(self):
        if self.heap:
            return str(self.heap)
        else:
            raise IndexError(self.EmptyErrorMessage)