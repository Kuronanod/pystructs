# สร้าง Node สำหรับ Deque

class DequeNode:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None