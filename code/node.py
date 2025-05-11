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

    def setSuffixLink(self, other: "Node"): 
        self.suffixLink = other

    def __str__(self): 
        return f"{self.stringTuple}" if self.stringTuple is not None else "root"

    def __repr__(self): 
        return f"{self.stringTuple}" if self.stringTuple is not None else "root"

    def __eq__(self, other: "Node"):

        if not isinstance(other, Node): 
            return False 
        return ( other.stringTuple == self.stringTuple and 
                other.suffixLink == self.suffixLink and 
                sorted(other.children.items()) == sorted(self.children.items()) )


if __name__ == "__main__": 
    pass 
    
