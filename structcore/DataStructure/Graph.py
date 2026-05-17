# Import Node For Graph Method
from structcore.DataStructure.Deque import Deque

class Graph:

    # Error Message
    EmptyErrorMessage = "This Value Is Empty"
    IndexOutOfRange = "Index Is Out Of Range"
    ValueErrorMessage = "Value Not Found"
    
    # Constructor
    def __init__(self,is_directed = True):
        self.graph = {}
        self.is_directed = is_directed

    # Class Method for Undirected Graph
    @classmethod
    def undirected(cls):
        return cls(False)
    
    # Class Method for Directed Graph
    @classmethod
    def directed(cls):
        return cls(True)

    # Depth_First_Search Meyhod (Private) : Performs Depth First Search traversal on the Object
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
    
    # Breadth_First_Search Method (Private) : Performs Breadth First Search traversal on the Object
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

    # Add_Vertex Method : Adds a vertex to the Object
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add_Edge Method : Adds an edge to the specified vertex
    def add_edge(self,vertex1,vertex2):
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
            if not self.is_directed:
                self.graph[vertex2].append(vertex1)

    # Get_Neighbours Method : Retrieves all edges from the specified vertex
    def get_neighbours(self,vertex):
        return self.graph[vertex]
    
    # Has_vertex Method : Checks whether the specified vertex exists in the Object
    def has_vertex(self,vertex):
        if vertex in self.graph:
            return True
        else:
            return False

    # Has_Edge Method : Checks whether the specified edge exists in the vertex
    def has_edge(self,vertex1,vertex2):
        if vertex1 in self.graph:
            return vertex2 in self.graph[vertex1]
        return False

    # Remove_Vertex Method : Removes the specified vertex from the Object
    def remove_vertex(self,vertex):
        if not self.graph:
            raise IndexError(self.EmptyErrorMessage)
        if vertex in self.graph:
            self.graph.pop(vertex)
            for i in self.graph:
                if vertex in self.graph[i]:
                    self.graph[i].remove(vertex)

    # Remove_Edge Method : Removes the specified edge from the vertex
    def remove_edge(self,vertex1,vertex2):
        if vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            if not self.is_directed:
                self.graph[vertex2].remove(vertex1)

    # Clear Method : Removes all data from the Object
    def clear(self):
        self.graph.clear()

    # IsEmpty Method : Checks whether the Object is empty
    def isEmpty(self):
        if not self.graph:
            return True
        else:
            return False
        
    # GetItem Method : Accesses values in the Object using a key via `[]` (returns edges from that vertex)
    def __getitem__(self, key):
        if key not in self.graph:
            raise IndexError(self.ValueErrorMessage)
        return self.get_neighbours(key)
        
    # Len Method : Returns the total number of vertices in the Object
    def __len__(self):
        return len(self.graph)
    
    # Contains Method : Checks if a specific vertex exists in the Object using the `in` keyword
    def __contains__(self, vertex):
        if vertex in self.graph.keys():
            return True
        else:
            return False
        
    # Eq Method : Compares two Objects to determine if they are the same class and have identical data
    def __eq__(self, object):
        if not isinstance(object,Graph):
            return False
        else:
            return self.graph == object.graph and self.is_directed == object.is_directed
        
    # Iter Method : Iterates through each vertex in the Object by yielding values one by one
    def __iter__(self):
        return iter(self.graph)

    # Repr Method : Displays the Object type when the `repr()` function is called
    def __repr__(self):
        return f"{self.__class__.__name__}({self.graph})"
    
    # Bool Method : Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
    def __bool__(self):
        return bool(self.graph)

    # Str Method : Displays all values within the Object
    def __str__(self):
        return str(self.graph)