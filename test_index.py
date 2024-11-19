import unittest
import index


class test_addFuntion(unittest.TestCase):
    
    def test_add_positive_number(self):
        result = index.add(1, 2)
        self.assertEqual(result , 3)
        
    def test_add_negative_number(self):
        result = index.substruct(-1, -2)
        
        self.assertEqual(result , -3)
        
    def test_add_mixed_number(self):
        result1 = index.add(1, -2)
        result2 = index.add(-1, 2)
        
        self.assertEqual(result1, -1)
        self.assertEqual(result2, 1)
        

class test_word(unittest.TestCase):
    
    def test_upper_string(self):
        result = index.upperString("abdelakder")
        self.assertTrue(result, "ABDELAKDER")
    
    def test_isupper(self):
        result = index.checkUpper("abdelakder")
        self.assertTrue(result, "ABDELAKDER")
    

if __name__ == '__main__':
    unittest.main()