# Import Helper Method For DepthFirstSearch
from structcore.DataStructure.BinarySearchTree import BinarySearchTree
from structcore.DataStructure.LinkedList import LinkedList
from structcore.DataStructure.Graph import Graph
from structcore.DataStructure.Trie import Trie

# Depth First Search : Search item in object with depth first search algorithm

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
