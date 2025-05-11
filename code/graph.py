from node import Node 

class Graph: 

    def __init__(self): 
        
        self.graph1 = self.createABAC()

    def createABAC(self): 

        root = Node()
        root.setSuffixLink(root)

        # layer 1: 
        u = Node()
        u.setTuple(0,1)
        u.setSuffixLink(root)
        
        leaf2 = Node()
        leaf2.setTuple(1,5)

        leaf4 = Node()
        leaf4.setTuple(3,5)

        root.add_child("a", u)
        root.add_child("b", leaf2)
        root.add_child("c", leaf4)

        #layer 2: 
        leaf1 = Node()
        leaf1.setTuple(1,5)

        leaf3 = Node()
        leaf3.setTuple(3,5)

        u.add_child("b", leaf1)
        u.add_child("c", leaf3)

        return root 

    def dfs_print(self, root): 

        order = []

        def traverse(root): 

            order.append(root)

            if ( len(root.children) == 0): 
                return 

            # traverse in alphbetical order 
            node_list = sorted(root.children.items(), 
                               key=lambda x: x[0]) 

            for char, node in node_list:  
                traverse(node)
        
        traverse(root)
        return order


if __name__ == "__main__":  
    
    abac = Graph() 
    start = abac.createABAC()
    print(abac.dfs_print(start))


