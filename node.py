from typing import * 

class Node(): 

    def __init__(self): 
        self.stringTuple = None
        self.totalLength = 0 
        self.suffixLink = None 
        self.children = {} # used to allow us to determine the path in skip counting (pg22)  
        self.parent = None 
    
    def set_suffix(self, extensionPoint: "Node"): 
        self.suffixLink = extensionPoint  

    def add_child(self, char: str, child: "Node"): 
        self.children[char] = child 

    def setTuple(self, start: int, end: int): 
        self.stringTuple = [start, end]

    def suffix_extension1(self): 
        self.stringTuple[1] += 1 
    
    def set_length(self, length: int): 
        self.length = length