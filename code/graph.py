from node import Node 

class Graph: 

    def __init__(self, selection): 

        self.root = Node()
        self.root.setSuffixLink(self.root)
        self.string = None 

        if (selection == 0): 
            self.root = self.createABAC() 
            self.string = "abac$"
        elif (selection == 1): 
            self.root = self.createABACACBAD()
            self.string = "abacabad$"

    def createABAC(self): 

        # layer 1: 
        u = Node()
        u.setTuple(0,1)
        u.setSuffixLink(self.root)
        
        leaf2 = Node()
        leaf2.setTuple(1,5)

        leaf4 = Node()
        leaf4.setTuple(3,5)

        self.root.add_child("a", u)
        self.root.add_child("b", leaf2)
        self.root.add_child("c", leaf4)

        #layer 2: 
        leaf1 = Node()
        leaf1.setTuple(1,5)

        leaf3 = Node()
        leaf3.setTuple(3,5)

        u.add_child("b", leaf1)
        u.add_child("c", leaf3)

        return self.root

    def createABACACBAD(self): 

        # under the root: 
        u, w, v = Node(), Node(), Node()

        # set the suffix links  
        u.setSuffixLink(self.root)
        v.setSuffixLink(w)
        w.setSuffixLink(u)

        # set the children of the root: 
        u.setTuple(0,1)
        w.setTuple(1,3)

        leaf8 = Node() 
        leaf4 = Node() 
        leaf4.setTuple(3,9)
        leaf8.setTuple(7,9)

        self.root.add_child("a",u)
        self.root.add_child("b", w)
        self.root.add_child("d", leaf8)
        self.root.add_child("c", leaf4)

        # set the children under u: 
        leaf7, leaf3, = Node(), Node() 
        leaf3 = leaf4 
        leaf7 = leaf8 
        v.setTuple(1,3)

        u.add_child("c", leaf3)
        u.add_child("d", leaf7)
        u.add_child("b", v)

        # set the children under v: 
        leaf5 = leaf7 
        leaf1 = leaf4 
        v.add_child("c", leaf1)
        v.add_child("d", leaf5)

        # set the children under w: 
        leaf6 = leaf7 
        leaf2 = leaf1 
        w.add_child("c", leaf2)
        w.add_child("d", leaf6)

        return self.root

    def dfs_print(self): 

        order = []

        def traverse(root): 

            order.append(root)

            if (len(root.children) == 0): 
                return 

            # traverse in alphbetical order 
            node_list = sorted(root.children.items(), 
                               key=lambda x: x[0]) 

            for char, node in node_list:  
                traverse(node)
        
        traverse(self.root)
        return order

    def string_suffix(self): 
        res = self.dfs_print() 

        for t in res: 
            if t.stringTuple is not None: 
                left, right = t.stringTuple 
                string_slice = self.string[left:right]
                print(string_slice)
            else:
                print("root")
    


if __name__ == "__main__":  

    g = Graph(0)
    g.string_suffix()

    
