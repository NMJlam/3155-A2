from typing import * 

class Node(): 

    def __init__(self): 
        self.stringTuple = None
        self.totalLength = 0 
        self.suffixLink = None 
        self.children = {} # used to allow us to determine the path in skip counting (pg22)  
        self.parent = None 

    def add_child(self, char: str, child: "Node"): 
        self.children[char] = child 

    def setTuple(self, start: int, end: int): 
        self.stringTuple = [start, end]

    def suffix_extension1(self): 
        if self.stringTuple is not None: 
            self.stringTuple[1] += 1 
    
    def length(self): 
        return self.stringTuple[1] - self.stringTuple[0] + 1 if self.stringTuple is not None else 0 
