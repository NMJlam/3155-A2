from node import Node 
from typing import * 

class Ukkonens: 

    def __init__(self, string: str): 
        self.root = Node() 
        self.string = string + "$"

        self.active
    
    def construct(self) -> None: 

        n = len(self.string)
        globalEnd = 0 

        for i in range(n-1): 

            globalEnd+=1

            for j in range(i+1): 
                
                self.traverse(self.root, i-j, j) # traversing from the root to an extension point 
        
    def traverse(self, start: Node, remainder: int, char_idx: int) -> Node: 
        # [starting node] - start 
        # [remainder] - can either be the length of the string or the remainder after we subtracted 
        # [char_idx] - letter of the curren string 
        # TODO
        # can be subject to change if following a suffix link 
        # what if we have a remainder that is valid BUT we also mismatch but the indexed string invalid

        # implement the skipcounting strategy 
        # note that each edge holds one less because we have the first letter in the parent nodes dictionary 

        curr = start 
        currIDX = char_idx

        # checks if there are children 
        # checks if there is a valid direction in which we can traverse 
        while ( remainder > 0 ): 
            
            char = self.string[currIDX]

            if char not in curr.children: 
                break 

            valid_child = curr.children[char] 

            # get the length of the edge 
            edge_length = valid_child.stringTuple[1] - valid_child.stringTuple[0] + 1 # not sure about this +1 
            
            if edge_length > remainder: 
                self.active = curr 
                return curr # extension point 
            
            # update the variables such that the remainder and the character:
            remainder -= edge_length # remainder - will be less than the total path traversed 
            currIDX += edge_length # character - is the current one we are traversing  

            curr = valid_child 
        
        self.active = curr.parent or curr 
        return curr # extension point  





            

            











            

            
            
            

        