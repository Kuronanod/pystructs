from Deque import Deque

class Graph:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"
    
    # Constructor
    def __init__(self,is_directed = True):
        self.graph = {}
        self.is_directed = is_directed

    # Class Method สำหรับ Undirected Graph
    @classmethod
    def undirected(cls):
        return cls(False)
    
    # Class Method สำหรับ Directed Graph
    @classmethod
    def directed(cls):
        return cls(True)

    # Depth_First_Search Meyhod (Private) : เรียงข้อมูลแบบ DepthFirstSearch สำหรับ Object
    def _depth_first_search(self,value):

        if not self.graph:
            return False
        
        visited = set()
        start = next(iter(self.graph))

        stack = [start]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            if node == value:
                return True
            
            for neighbour in self.graph.get(node,[]):
                if neighbour not in visited:
                    stack.append(neighbour)

        return False
    
    # Breadth_First_Search Method (Private) : เรียงข้อมูลแบบ BreadthFirstSearch สำหรับ Object
    def _breadth_first_search(self,value):

        if not self.graph:
            return False
        
        visited = set()
        start = next(iter(self.graph))

        deque = Deque()
        deque.append(start)

        while Deque:

            node = Deque.popleft()

            if node in visited:
                continue

            visited.add(node)

            if node == value:
                return True

            for neighbour in self.graph.children():
                if neighbour not in visited:
                    deque.append(neighbour)
            
        return False

    # Add_Vertex Method : เพิ่ม Vertex ใหม่ลงไปใน Object
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add_Edge Method : เพิ่ม Edge เข้าไปใน Vertex ที่ต้องการ
    def add_edge(self,vertex1,vertex2):
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
            if not self.is_directed:
                self.graph[vertex2].append(vertex1)

    # Get_Neighbours Method : Return Edge ทั้งหมดที่อยู่ใน Vertex ที่ต้องการ
    def get_neighbours(self,vertex):
        return self.graph[vertex]
    
    # Has_vertex Method : ตรวจสอบว่ามี Vertex นี้ใน Object ไหม
    def has_vertex(self,vertex):
        if vertex in self.graph:
            return True
        else:
            return False

    # Has_Edge Method : ตรวจสอบว่าใน Vertex ที่ต้องการตรวจสอบมี Edge ที่ต้องการตรวจสอบอยู่ไหม
    def has_edge(self,vertex1,vertex2):
        if vertex1 in self.graph:
            return vertex2 in self.graph[vertex1]
        return False

    # Remove_Vertex Method : ทำการลบ Vertex ที่ต้องการใน Object
    def remove_vertex(self,vertex):
        if not self.graph:
            raise IndexError(self.EmptyErrorMessage)
        if vertex in self.graph:
            self.graph.pop(vertex)
            for i in self.graph:
                if vertex in self.graph[i]:
                    self.graph[i].remove(vertex)

    # Remove_Edge Method : ทำการลบ Edge ที่ต้องการใน Vertex
    def remove_edge(self,vertex1,vertex2):
        if vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            if not self.is_directed:
                self.graph[vertex2].remove(vertex1)

    # Clear Method : ทำการลบข้อมูลทั้งหมใน Object
    def clear(self):
        self.graph.clear()

    # IsEmpty Method : ทำการตรวจสอบว่า Object นี้นั้นเป็นค่าว่างไหม
    def isEmpty(self):
        if not self.graph:
            return True
        else:
            return False
        
    # GetItem Method : เข้าถึงค่าใน Object ผ่าน Key โดยใช้ [] ซึ่งจะ Return Edge ที่อยู่ใน Vertex นั้น
    def __getitem__(self, key):
        if key not in self.graph:
            raise IndexError(self.ValueErrorMessage)
        return self.get_neighbours(key)
        
    # Len Method : หาจำนวน Vertex ทั้งหมดใน Object แล้ว Return ค่า
    def __len__(self):
        return len(self.graph)
    
    # Contains Method : ตรวจสอบว่ามี Vertex ดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
    def __contains__(self, vertex):
        if vertex in self.graph.keys():
            return True
        else:
            return False
        
    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและค่าใน Object ทั้งหมดเหมือนกันไหม
    def __eq__(self, object):
        if not isinstance(object,Graph):
            return False
        else:
            return self.graph == object.graph and self.is_directed == object.is_directed
        
    # Iter Method : เข้าถึงข้อมูลใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        return iter(self.graph)

    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr() 
    def __repr__(self):
        return f"{self.__class__.__name__}({self.graph})"
    
    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return bool(self.graph)

    # Str Method : แสดงผลค่าใน Object ทั้งหมด
    def __str__(self):
        return str(self.graph)