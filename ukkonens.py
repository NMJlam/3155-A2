from node import Node 
from typing import * 

class Ukkonens: 

    def __init__(self, string: str): 
        self.root = Node() 
        self.string = string + "$"

        # NOTE: The active node is the node at which we are doing the extension  
        # NOTE: the Active node is the starting point of every traversal 
        self.active = None 
        self.pending = self.root 
        self.showstopper = False  
        self.internal_created =  False 

    def construct(self) -> Node: 

        n = len(self.string)
        globalEnd = 0 
        start = self.root

        for i in range(n): 

            globalEnd+=1

            for j in range(i): 

                remainder = self.traverse(start, i, j)
                self.make_extension(i, j, remainder, globalEnd)

                if ( self.showstopper ): 
                    break 

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

    def make_extension(self, i: int, j:int, remainder : Tuple[int, int], globalEnd : int) -> None: 
        '''
        Determine which extension we need to make based on the conditions of the active node
        Case 1: Extension of the leaf 
        Case 2a: Extension on a node 
        Case 2b: Extension on an edge 
        Case 3: Do Nothing 
        '''

        # break down the remainder to its length 
        rem_start, rem_end = remainder 
        rem_len = rem_end - rem_start
        
        # NOTE: Case 2.1
        # first character of the remainder
        char = self.string[rem_start]
        
        # This indicates that we have fallen on the active node -> 2.1
        if ( rem == 0 and 
            char not in self.active.children): 

            self.internal_created = False 

            # this is an example of extension 2.1 
            extension1 = Node()
            extension1.setTuple(rem_start, globalEnd)
            self.active.add_child(char, extension1)
        
        # NOTE: Case 2.2
        # character at the point of traversal 
        child = self.active.children[char]
        child_start, child_end = child.stringTuple
        edge_char = child_start + rem_len - 1 #TODO verify 
        rem_char = j + rem_len - 1 # TODO: verify 

        # This indicates that we have fallen on an edge -> 2.2 
        if ( rem > 0 and 
               self.string[edge_char] != self.string[rem_char] ): 

            self.internal_created = True 
            
            # create 2 nodes: 1 for the existing path and the new one 
            ex_path, new_path = Node(), Node() 

            # set the start and ends of the children 
            child.setTuple(child_start, edge_char -1)
            ex_path.setTuple(edge_char, globalEnd)
            new_path.setTuple(rem_char, globalEnd)

            # put the children under the children node: 
            child.add_child(self.string[edge_char], ex_path) # existing path 
            child.add_child(self.string[rem_char], new_path) # new path 

            # set the newly created node to the pending node 
            self.pending = child

        # TODO: verify that the rule 3 extension is always the last extension 
        if ( self.string[edge_char] == self.string[rem_char]):
            self.internal_created = False 
            self.showstopper = True 


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



    
