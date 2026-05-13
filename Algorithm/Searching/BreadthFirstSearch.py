from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.LinkedList import LinkedList
from DataStructure.Graph import Graph
from DataStructure.Trie import Trie

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