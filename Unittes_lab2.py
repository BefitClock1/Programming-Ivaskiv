import unittest
from lab2 import largest_min_distance

class TestLargestMinDistance(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largest_min_distance(5, 3, [1, 2, 8, 4, 9]), 3)
    
    def test_case_2(self):
        self.assertEqual(largest_min_distance(5, 3, [1, 2, 4, 8, 9]), 3)
    
    def test_case_3(self):
        self.assertEqual(largest_min_distance(6, 4, [1, 2, 4, 8, 9, 10]), 2)

if __name__ == "__main__":
    unittest.main()