from graph import Graph
import unittest 
from ukkonens import Ukkonens 

class testUkkonens(unittest.TestCase): 

    def traversal_check(self, expected: "Node", actual: "Node") -> bool: 

        if (expected != actual): 
            return False 

        actual_children = sorted(actual.children.items(), key=lambda x: x[0]) 
        expected_children = sorted(expected.children.items(), key=lambda x: x[0]) 

        if (len(actual_children) != len(expected_children)):
            return False 

        for i in range( len(actual_children)): 

            _, achild = actual_children[i]
            _, echild = expected_children[i]

            if (not self.traversal_check(achild, echild) ):
                return False 

        return True 

    def test_abac(self): 

        g = Graph(0)
        string_g  = g.string
        expected = Ukkonens("abac") 

        self.assertEqual( self.traversal_check (g.root, expected.root), 
                            True)

    def test_abacabad(self): 
        g = Graph(1)
        string_g  = g.string
        expected = Ukkonens("abacabad") 

        self.assertEqual( self.traversal_check (g.root, expected.root), 
                            True)


if __name__ == "__main__": 
    unittest.main() 




