from node import Node 
from typing import * 

class Ukkonens: 

    def __init__(self, string: str): 
        self.root = Node() 
        self.string = string + "$"

        # NOTE: The active node is the node at which we are doing the extension  
        # NOTE: the Active node is the starting point of every traversal 
        self.active = None 
        self.pending = None

    def construct(self) -> Node: 

        n = len(self.string)
        globalEnd = 0 
        start = self.root

        for i in range(n): 

            globalEnd+=1

            for j in range(i): 

                remainder = self.traverse(start, i, j)
                self.make_extension(remainder, globalEnd)

        return self.root 

    def traverse(self, start: "Node", i:int, j:int) -> Tuple[int, int]: 
        """
        sets the active node based on find the conditions of case 2.1 & 2.2
        returns the remainder tuple (start: end) - this should also be the slice of the string

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
                break 

            curr = child 
            j += edge_length
            rem -= edge_length

        self.active = curr 
        return j,i 

    def make_extension(self, remainder : Tuple[int, int], globalEnd : int) -> None: 
        '''
        Determine which extension we need to make based on the conditions of the active node
        Case 1: Extension of the leaf 
        Case 2a: Extension on a node 
        Case 2b: Extension on an edge 
        Case 3: Do Nothing 
        '''

        rem_start, rem_end = remainder 
        char = self.string[rem_start]
        
        # TODO: finish extensions 
        # TODO: check if extension1 is valid or not 

        if ( char not in self.active.children):

            extension1 = Node()
            extension1.setTuple(rem_start, globalEnd)
            self.active.add_child(char, extension1)


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

    string = "ab"
    u = Ukkonens(string)
    u.construct()
    print(u.active)
    print(u.root.children)
    print(string[0:2])
    print(string[1:3])



    
