##### PyStructs

A comprehensive Python library for **Data Structures** and **Algorithms**.

### Installation

```bash

pip install pystructs

```

### Requirement

Python version 3.8 or higher

### Available DataStructure

- Linked List
- Stack
- Queue
- Deque
- Binary Search Tree
- Heap (Min/Max)
- Graph (Directed/Undirected)
- Trie

-------------------------------------------------------------------------------------

## Linked List
# Private Methods
- `depth_first_search`: Used for traversing data using Depth First Search within the Object
- `breadth_first_search` : Used for traversing data using Breadth First Search within the Object

# Public Methods
- `append`: Adds an element to the end (tail) of the Object
- `appendleft`: Adds an element to the front (head) of the Object
- `insert`: Inserts data at the specified position and existing node at that position shifts to the right
- `pop`: Removes the last element from the Object and returns the removed value
- `popleft`: Removes the first element from the Object and returns the removed value
- `remove`: Removes the node at the specified index in the Object
- `find`: Finds the first occurrence of a value and returns the index of that node
- `reverse`: Reorders the nodes in the Object by reversing the order (back to front)
- `min` : Find a minimum value in object and return
- `max` : Find a maximum value in object and return
- `clear`: Removes all nodes from the Object

# Python Magic Methods
- `__getitem__`: Accesses a node value within the Object using a key via `[]`
- `__setitem__`: Modifies a node value within the Object using a key via `[]`
- `__len__`: Returns the total number of nodes in the Object
- `__contains__`: Checks if a specific value exists in the Object using the `in` keyword
- `__iter__`: Iterates through each node in the Object by yielding values one by one
- `__eq__`: Compares two Objects to determine if they are the same class and have identical nodes
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object when printed

-------------------------------------------------------------------------------------

## Stack
# Public Methods
- `push`: Adds a new node to the top of the Object
- `update`: Modifies the data of the top node in the Object
- `peek`: Accesses and returns the data of the top node in the Object
- `pop`: Removes the top node from the Object
- `clear`: Removes all nodes from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__len__`: Returns the total number of nodes in the Object
- `__iter__`: Iterates through each node in the Object by yielding values one by one
- `__contains__`: Checks if a specific value exists in the Object using the `in` keyword
- `__eq__`: Compares two Objects to determine if they are the same class and have identical nodes
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

## Queue
# Public Methods
- `enqueue`: Adds a node to the front of the Object
- `dequeue`: Removes a node from the rear of the Object
- `peek`: Views the data at the front of the Object
- `clear`: Removes all nodes from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__len__`: Returns the total number of nodes in the Object
- `__iter__`: Iterates through each node in the Object by yielding values one by one
- `__contains__`: Checks if a specific value exists in the Object using the `in` keyword
- `__eq__`: Compares two Objects to determine if they are the same class and have identical nodes
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

## Deque
# Public Methods
- `append`: Adds a node to the rear (tail) of the Object
- `appendleft`: Adds a node to the front (head) of the Object
- `set_head`: Modifies the data of the node at the front of the Object
- `set_tail`: Modifies the data of the node at the rear of the Object
- `peek`: Views the data of the node at the rear of the Object
- `peekleft`: Views the data of the node at the front of the Object
- `pop`: Removes the node from the rear of the Object
- `popleft`: Removes the node from the front of the Object
- `clear`: Removes all nodes from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__getitem__`: Accesses a node's value within the Object using a key via `[]`
- `__len__`: Returns the total number of nodes in the Object
- `__contains__`: Checks if a specific value exists in the Object using the `in` keyword
- `__iter__`: Iterates through each node in the Object by yielding values one by one
- `__eq__`: Compares two Objects to determine if they are the same class and have identical nodes
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

## Binary Search Tree
# Private Methods
- `is_equal`: Checks whether two Objects are identical in both data and structure
- `inorder_asc_helper`: Helper method to collect data in ascending order
- `inorder_desc_helper`: Helper method to collect data in descending order
- `depth_first_search_recursive`: Helper method for Depth First Search traversal
- `depth_first_search`: Performs Depth First Search traversal on the Object
- `breadth_first_search`: Performs Breadth First Search traversal on the Object

# Public Methods
- `insert`: Adds a node to the Object
- `find`: Find a specific value within the Object
- `inorder_asc`: Returns values in ascending order
- `inorder_desc`: Returns values in descending order
- `min`: Returns the smallest value in the Object
- `max`: Returns the largest value in the Object
- `peek`: Views the top node (Root) and returns its value
- `remove`: Removes a specified node from the Object
- `clear`: Removes all nodes from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__len__`: Returns the total number of nodes in the Object
- `__contains__`: Checks if a specific value exists in the Object using the `in` keyword
- `__eq__`: Compares two Objects to determine if they are the same class and have identical values
- `__iter__`: Iterates through each value in the Object by yielding values one by one
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

## Heap
Heap is stored in a Python List.  
Values can be accessed using the following formulas, where `i` is the index of the element:
- **parent** = `(i - 1) // 2`
- **left child** = `2 * i + 1`
- **right child** = `2 * i + 2`
Heap is divided into two types:
- **Min Heap**: smallest value at the root
- **Max Heap**: largest value at the root
Both types store data in an array based on the formulas above.

# Class Methods
- `min_heap`: Creates a new Min Heap instance
- `max_heap`: Creates a new Max Heap instance

# Private Methods
- `heapify_up`: Organizes the Object to maintain heap property after inserting data
- `heapify_down`: Organizes the Object to maintain heap property after removing data

# Public Methods
- `push`: Adds data to the Object
- `peek`: Returns the top value of the Object without removing it
- `max`: Returns the maximum value in the Object
- `min`: Returns the minimum value in the Object
- `pop`: Removes and returns the top value of the Object
- `clear`: Removes all data from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__getitem__`: Accesses data in the Object using a key via `[]`
- `__len__`: Returns the total number of elements in the Object
- `__iter__`: Iterates through each value in the Object by yielding values one by one
- `__eq__`: Compares two Objects to determine if they are the same class and have identical values
- `__contains__`: Checks if a specific value exists in the Object using the `in` keyword
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

## Graph
Graph is divided into two classes:
- **Directed Graph**: edges have a direction (one-way)
- **Undirected Graph**: edges are bidirectional (two-way)

# Class Methods
- `Directed`: Creates a new Directed Graph instance
- `Undirected`: Creates a new Undirected Graph instance

# Private Methods
- `depth_first_search`: Performs Depth First Search traversal on the Object
- `breadth_first_search`: Performs Breadth First Search traversal on the Object

# Public Methods
- `add_vertex`: Adds a vertex to the Object
- `add_edge`: Adds an edge to the specified vertex
- `get_neighbors`: Retrieves all edges from the specified vertex
- `has_vertex`: Checks whether the specified vertex exists in the Object
- `has_edge`: Checks whether the specified edge exists in the vertex
- `remove_vertex`: Removes the specified vertex from the Object
- `remove_edge`: Removes the specified edge from the vertex
- `clear`: Removes all data from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__getitem__`: Accesses values in the Object using a key via `[]` (returns edges from that vertex)
- `__len__`: Returns the total number of vertices in the Object
- `__contains__`: Checks if a specific vertex exists in the Object using the `in` keyword
- `__eq__`: Compares two Objects to determine if they are the same class and have identical data
- `__iter__`: Iterates through each vertex in the Object by yielding values one by one
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

## Trie
# Private Methods
- `collect_word`: Helper method to collect specific data from the Object and return it
- `remove_helper`: Helper method to remove a word without disrupting the Object's structure
- `depth_first_search`: Performs Depth First Search traversal on the Object
- `depth_first_search_collect`: Helper method for collecting data during Depth First Search
- `breadth_first_search`: Performs Breadth First Search traversal on the Object

# Public Methods
- `insert`: Adds a word to the Object
- `find`: Find for a specific word in the Object
- `starts_with`: Checks if any word starts with the given prefix; returns `True` if found
- `get_word`: Retrieves all words from the Object and returns them
- `get_word_with_prefix`: Retrieves all words that start with the given prefix and returns them
- `remove`: Removes a specified word from the Object
- `clear`: Removes all data from the Object
- `isEmpty`: Checks whether the Object is empty

# Python Magic Methods
- `__len__`: Returns the total number of words in the Object
- `__contains__`: Checks if a specific word exists in the Object using the `in` keyword
- `__iter__`: Iterates through each word in the Object by yielding values one by one
- `__eq__`: Compares two Objects to determine if they are the same class and have identical values
- `__repr__`: Displays the Object type when the `repr()` function is called
- `__bool__`: Defines whether the Object evaluates to `True` or `False` when used directly in an `if` statement
- `__str__`: Displays all values within the Object

-------------------------------------------------------------------------------------

### Available Algorithm

Sort Type
- BubbleSort
- SelectionSort
- InsertionSort
- QuickSort
- MergeSort
- HeapSort

Search Type
- LinearSearch
- BinarySearch
- DepthFirstSearch
- BreadthFirstSearch

-------------------------------------------------------------------------------------

## Sort Type

# BubbleSort
# Public Function
- `bubble_sort`: Sorts items in the Object using the Bubble Sort Algorithm

# SelectionSort
# Public Function
- `selection_sort`: Sorts items in the Object using the Selection Sort Algorithm

# InsertionSort
# Public Function
- `insertion_sort`: Sorts items in the Object using the Insertion Sort Algorithm

# QuickSort
# Private Functions
- `__median_of_three`: Selects the pivot from the first, middle, and last elements of the partition
- `__quick_sort_in_place`: Sorts the Object in-place using recursive partitioning
- `__partition`: Rearranges items around the pivot into left and right partitions
# Public Function
- `quick_sort`: Sorts items in the Object using the Quick Sort Algorithm

## MergeSort
# Private Function
- `__merge`: Merges two sorted sublists into a single sorted list

# Public Function
- `merge_sort`: Sorts items in the Object using the Merge Sort Algorithm

# HeapSort
# Public Function
- `heap_sort`: Sorts items in the Object using the Heap Sort Algorithm

-------------------------------------------------------------------------------------

## Search Type

# Binary Search
# Public Function
- `binary_search`: Searches for a target value in the Object using the Binary Search Algorithm (requires sorted data)

# Breadth First Search
# Public Method
- `breadth_first_search`: Searches for a target value in the Object using the Breadth First Search Algorithm

# Depth First Search
# Public Method
- `depth_first_search`: Searches for a target value in the Object using the Depth First Search Algorithm

# Linear Search
# Public Function
- `linear_search`: Searches for a target value in the Object using the Linear Search Algorithm

-------------------------------------------------------------------------------------

## How To Use

import pystructs

data = pystructs.LinkedList()
data.append(20)
print(data)

message = pystructs.Trie()
message.insert("Kuronanod")
print(message.find("Kuronanod"))

data = [2,41,4,2,5,7,4,8744,7,345,7]
sorted_data = pystructs.quick_sort(data.copy())
answer = pystructs.linear_search(sorted_data,8744)
print(answer)

-------------------------------------------------------------------------------------

### License

MIT License

Copyright (c) 2026 Kuronanod

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Author

Thawankorn Suwannabon
Github : Kuronanod
Email : thwalkrsuwrrnbl@gmail.com
