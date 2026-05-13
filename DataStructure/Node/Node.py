# สร้าง Node สำหรับเป็น Linked List โดยจะเก็บค่าของ Data กับ Pointer

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None