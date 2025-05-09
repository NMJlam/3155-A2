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
        start = self.root

        for i in range(n): 

            globalEnd+=1

            for j in range(i): 

                self.traverse(start, i, j)

        return self.root 

    def traverse(self, start: "Node", i:int, j:int) -> None: 
        """
        sets the active node based on find the conditions of case 2.1 & 2.2

        We want to traverse to the point at which we are doing the extension (active node) 
            - This will allow us to perform the extensions at 2.1 or 2.2 
        NOTE: extension 1,3 are handled differently:
            1. Handled by the use of the globalEnd var, hence does not need to be encoded
            3. When we hit this extension we just terminate using the showstopper rule 
        """
        rem = i - j 
        curr = start 

        while ( rem > 0): 
            
            # get first character to decide direction and then find the children 
            char = self.string[j]

            if (char not in curr.children): 
                break 
            
            child = curr.children[char]

            # get the length of the traversal edge 
            edge_length = child.length()

            if (rem <= edge_length): 
                self.active = curr 
                break 

            curr = child 
            i += edge_length
            rem -= edge_length

        self.active = curr 

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
        pass 

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

if __name__ == "__main__": 

    string = "abac"
    u = Ukkonens(string)
    u.construct()
    print(u.active)


    
