from typing import * 

'''
The Node class: 
    - The tuple represents the slice of the string
    - The length is the length of the slice 
The children: 
    - Stored in a dictionary - key: char | value: node with full string slice 
'''

class Node: 

    def __init__(self): 
        self.stringTuple = None
        self.totalLength = 0 
        self.suffixLink = None 
        self.children = {} # used to allow us to determine the path in skip counting (pg22)  

    def add_child(self, char: str, child: "Node"): 
        self.children[char] = child 

    def setTuple(self, start: int, end: int): 
        self.stringTuple = [start, end]
    
    def length(self): 
        return self.stringTuple[1] - self.stringTuple[0]  if self.stringTuple is not None else 0 

    def __str__(self): 
        return self.stringTuple if self.stringTuple is not None else "root"

if __name__ == "__main__": 

    string = "abac" 
    node = Node() 
    node.setTuple(0,1)
    print(node.length()) 
    print(string[0:2])
