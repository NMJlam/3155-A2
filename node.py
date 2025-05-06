from typing import * 

class Node(): 

    def __init__(self): 
        self.stringTuple = None 
        self.length = None
        self.suffixLink = None 
    
    def set_suffix(self, extensionPoint: "Node"): 
        self.suffixLink = extensionPoint  