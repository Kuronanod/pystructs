from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.LinkedList import LinkedList
from DataStructure.Graph import Graph
from DataStructure.Trie import Trie

def depth_first_search(data,value,order = "inorder",node = None):

    WrongType = "Unsupported DataStructure"
    
    if isinstance(data,BinarySearchTree):
        data._depth_first_search(value,order)
    elif isinstance(data,LinkedList):
        data._depth_first_search(value)
    elif isinstance(data,Graph):
        data._depth_first_search(value,node)
    elif isinstance(data,Trie):
        data._depth_first_search(value)
    else:
        raise ValueError(WrongType)
