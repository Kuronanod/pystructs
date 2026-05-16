from pystructs.DataStructure.BinarySearchTree import BinarySearchTree
from pystructs.DataStructure.LinkedList import LinkedList
from pystructs.DataStructure.Graph import Graph
from pystructs.DataStructure.Trie import Trie

# Breadth First Search Function : Search item in object with breadth first search algorithm

def breadth_first_search(data,value):
    
    WrongType = "Unsupported DataStructure"

    if isinstance(data,BinarySearchTree):
        data._breadth_first_search(value)
    elif isinstance(data,LinkedList):
        data._breadth_first_search(value)
    elif isinstance(data,Graph):
        data._breadth_first_search(value)
    elif isinstance(data,Trie):
        data._breadth_first_search(value)
    else:
        raise IndexError(WrongType)