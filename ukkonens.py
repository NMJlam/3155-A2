from node import Node 
from typing import * 

class Ukkonens: 

    def __init__(self, string: str): 
        self.root = Node() 
        self.string = string + "$"

        # NOTE: The active node is the node at which we are doing the extension  
        # NOTE: the Active node is the starting point of every traversal 
        self.active = None 

    
    def construct(self) -> Node: 

        n = len(self.string)
        globalEnd = 0 

        for i in range(n): 

            globalEnd+=1

            for j in range(i): 
                
                extension_point, rem  = self.traverse(self.root, i-j, j) # traversing from the root to an extension point 
                    # NOTE: here we have i-j as the length of the suffix that we wish to insert 
                    # NOTE: j is the index of the character that we want to add 

                self.make_extension(i, rem, extension_point)
                self.resolveSuffixLinks()
                self.moveToNextExtension()
        
        return self.root 
        
    def traverse(self, start: Node, remainder: int, char_idx: int) -> Tuple[Node, int]: 
        # NOTE: we do not mention extension 1 only because the global end takes care of it  
        curr, rem, = start, remainder

        while (rem > 0): 

            char = self.string[char_idx]
            child = curr.children[char]
            edge_length = child.length()

            # case by case: 
            if 0 < rem < edge_length: 
                return child, rem # landing in between an edge 
            if rem == edge_length: 
                curr = child 
                rem = 0 # landing directly on the end of edge -> this means case 2,1
                break
            
            rem -= edge_length
            curr = child 
            self.active = curr # TODO: active node is what you have previously traversed 
            char_idx += edge_length

        return curr, rem  

   
    def make_extension(self, char_idx: int, remainder: int, extension_point: Node) -> None: 
        '''
        r < L:
            if compare the character along the where the remainder takes you to on the edge:
                same -> extension 3 
                diff -> extension 2 case 2
        r = 0: 
            if the current letter isnt inside the children -> extension 2 case 1
        r > L: 
            if child is a leaf -> extension 1 
        '''
        return 
    
    def resolveSuffixLinks(self) -> None: 
        # NOTE: Whenver you create a new internal node its suffix link is resolved in the next iteration - by the active node,  
        # case 2a: An
        # case 2b: Internal 
        # case 3: AN 
        # the only exception is when you make the first internal node 
        pass 

    def moveToNextExtension(self) -> None: 
        # NOTE: traverse suffix link 
        # NOTE: if the suffix link lead to the root chop one off the start
        pass 

