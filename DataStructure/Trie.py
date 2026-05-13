from Node import TrieNode
from Deque import Deque

class Trie:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0

    # Collect_Word Method (Private) : ช่วยเก็บค่าข้อมูลที่ต้องการใน Object แล้ว Return ค่า
    def _collect_word (self,node,current_word,word):
        if node.is_end:
            word.append(current_word)
        for character , child in node.children.items():
            self._collect_word(child , current_word + character , word)

    # Remove Helper Method (Private) : ลบคำที่ต้องการในโครงสร้างโดยที่ไม่ให้กระทบกับโครงสร้างของ Object
    def _remove_helper(self,node,word,index):
        if index == len(word):
            if not node.is_end:
                return False
            
            node.is_end = False
            return len(node.children) == 0
        
        character = word[index]
        if character not in node.children:
            return False
        
        child = node.children[character]
        remove_child = self._remove_helper(child,word,index + 1)

        if remove_child:
            del node.children[character]
            return len(node.children) == 0 and not node.is_end
        
        return False

    # Depth_First_search Method (Private) : เรียงข้อมูลแบบ DepthFirstSearch สำหรับ Object
    def _depth_first_search(self , prefix = "" ):

        word = []
        current = self.root

        for character in prefix:
            if character not in current.children:
                return word
            current = current.children[character]

        self._depth_first_search_collect(current , prefix , word)
        return word
    
    # Depth_First_Search_Collect Method (Private) : ช่วยเรียงข้อมูลแบบ DepthFirstSearch สำหรับ Object
    def _depth_first_search_collect(self , node , current_word , word):

        if node.is_end:
            word.append(current_word)

        for character , child in node.children.items():
            self._depth_first_search_collect(child , current_word + character , word)

    # Breadth_First_Search Method (Private) : เรียงข้อมูลแบบ BreadthFirstSearch สำหรับ Object
    def _breadth_first_search(self , prefix = ""):

        word = []

        current = self.root

        for character in prefix:
            if character not in current.children:
                return word
            current = current.children[character]

        deque = Deque()
        deque.append((current , prefix))

        while not deque.isEmpty():
            node , current_word = deque.popleft()

            if node.is_end():
                word.append(current_word)

            for character , child in node.children.items():
                deque.append((child , current_word + character))

        return word

    # Insert Method : เพิ่มคำที่ต้องการลงใน Object
    def insert(self,word):
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        if not current.is_end:
            current.is_end = True
            self.word_count += 1

    # Search Method : ค้นหาคำที่ต้องการใน Object
    def search(self,word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.is_end

    # Start_With Method : ค้นหาว่ามีคำที่ขึ้นต้นด้วยคำที่ต้องการไหมถ้ามีให้ Return True
    def start_with(self,prefix):
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

    # Get_word Method : หาคำทั้งหมดใน Object แล้ว Return ค่า
    def get_word(self):
        word = []
        self._collect_word(self.root,"",word)
        return word

    # Get_Word_With_Prefix Method : หาคำที่ขึ้นต้นด้วยคำที่ต้องการแล้ว Return ค่า
    def get_word_with_prefix(self,prefix):
        current = self.root
        for character in prefix:
            if character not in current.children:
                return []
            current = current.children[character]
        word = []
        self._collect_word(current,prefix,word)
        return word

    # Remove Method : ลบคำที่ต้องการออกจาก Object
    def remove(self,word):
        if not self.search(word):
            return False
        self._remove_helper(self.root,word,0)
        self.word_count -= 1
        return True

    # Clear Method : ลบข้อมูลทั้งหมดใน Object
    def clear(self):
        self.root = TrieNode()
        self.word_count = 0

    # IsEmpty Method : ตรวจสอบว่า Object นี้เป็นค่าว่างหรือไม่
    def isEmpty(self):
        if self.word_count == 0:
            return True
        else:
            return False
        
    # Len Method : หาจำนวนคำทั้งหมดใน Object แล้ว Return ค่า
    def __len__(self):
        return self.word_count
    
    # Contains Method : ตรวจสอบว่ามีค่าดังกล่าวใน Object นี้ไหมผ่านคำสั่ง in
    def __contains__(self, word):
        return self.search(word)
    
    # Iter Method : เข้าถึงข้อมูลใน Object แต่ละตัวโดยการวนลูปและ Yield ค่าคืนทีละตัว
    def __iter__(self):
        return iter(self.get_word())
    
    # Eq Method : เปรียบเทียบ Object สองตัวว่าเป็น Class เดียวกันและค่าใน Object เหมือนกันไหม
    def __eq__(self, object):
        if not isinstance(object,Trie):
            return False
        else:
            if self.get_word() == object.get_word():
                return True
            else:
                return False
    
    # Repr Method : แสดงผล Type ของ Object ผ่านฟังก์ชั่น repr()
    def __repr__(self):
        return f"Trie({self.get_word()})"
    
    # Bool Method : กำหนดค่าว่า Object จะเป็น True หรือ False เมื่อใช้งานกับ If โดยตรง
    def __bool__(self):
        return self.word_count > 0

    # Str Method : แสดงผลค่าใน Object ทั้งหมด
    def __str__(self):
        if self.isEmpty():
            raise IndexError(self.EmptyErrorMessage)
        else:
            return str(self.get_word())