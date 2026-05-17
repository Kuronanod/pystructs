# Import Node For Trie
from structcore.DataStructure.Node import TrieNode
from structcore.DataStructure.Deque import Deque

class Trie:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"

    # Constructor
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0

    # Collect_Word Method (Private) : Helper method to collect specific data from the Object and return it
    def _collect_word (self,node,current_word,word):
        if node.is_end:
            word.append(current_word)
        for character , child in node.children.items():
            self._collect_word(child , current_word + character , word)

    # Remove Helper Method (Private) : Helper method to remove a word without disrupting the Object's structure
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

    # Depth_First_search Method (Private) : Performs Depth First Search traversal on the Object
    def _depth_first_search(self , prefix = "" ):

        word = []
        current = self.root

        for character in prefix:
            if character not in current.children:
                return word
            current = current.children[character]

        self._depth_first_search_collect(current , prefix , word)
        return word
    
    # Depth_First_Search_Collect Method (Private) : Helper method for collecting data during Depth First Search
    def _depth_first_search_collect(self , node , current_word , word):

        if node.is_end:
            word.append(current_word)

        for character , child in node.children.items():
            self._depth_first_search_collect(child , current_word + character , word)

    # Breadth_First_Search Method (Private) : Performs Breadth First Search traversal on the Object
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

    # Insert Method : Adds a word to the Object
    def insert(self,word):
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        if not current.is_end:
            current.is_end = True
            self.word_count += 1

    # Find Method : Find for a specific word in the Object
    def find(self,word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.is_end

    # Start_With Method : Checks if any word starts with the given prefix; returns `True` if found
    def start_with(self,prefix):
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

    # Get_word Method : Retrieves all words from the Object and returns them
    def get_word(self):
        word = []
        self._collect_word(self.root,"",word)
        return word

    # Get_Word_With_Prefix Method : Retrieves all words that start with the given prefix and returns them
    def get_word_with_prefix(self,prefix):
        current = self.root
        for character in prefix:
            if character not in current.children:
                return []
            current = current.children[character]
        word = []
        self._collect_word(current,prefix,word)
        return word

    # Remove Method : Removes a specified word from the Object
    def remove(self,word):
        if not self.search(word):
            return False
        self._remove_helper(self.root,word,0)
        self.word_count -= 1
        return True

    # Clear Method : Removes all data from the Object
    def clear(self):
        self.root = TrieNode()
        self.word_count = 0

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if self.word_count == 0:
            return True
        else:
            return False
        
    # Len Method : Returns the total number of words in the Object
    def __len__(self):
        return self.word_count
    
    # Contains Method : Checks if a specific word exists in the Object using the `in` keyword
    def __contains__(self, word):
        return self.search(word)
    
    # Iter Method : Iterates through each word in the Object by yielding values one by one
    def __iter__(self):
        return iter(self.get_word())
    
    # Eq Method : Compares two Objects to determine if they are the same class and have identical values
    def __eq__(self, object):
        if not isinstance(object,Trie):
            return False
        else:
            if self.get_word() == object.get_word():
                return True
            else:
                return False
    
    # Repr Method : Displays the Object type when the `repr()` function is called
    def __repr__(self):
        return f"Trie({self.get_word()})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return self.word_count > 0

    # Str Method : Displays all values within the Object
    def __str__(self):
        if self.isEmpty():
            raise IndexError(self.EmptyErrorMessage)
        else:
            return str(self.get_word())