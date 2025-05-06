import typing 
from node import Node 

class Ukkonens: 

    def __init__(self): 
        self.root = Node() 
        
        # variables relevant to suffix links: 
        self.active = self.root 
        self.pending = None 
    
    def construct(self, string: str) -> None: 

        string += "$"
        n = len(string)
        for i in range(n): 

            i+=1 

        