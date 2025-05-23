import unittest
from Lab1 import longest_peak

class TestLongestPeak(unittest.TestCase):
    def test_single_peak(self):
        self.assertEqual(longest_peak([1, 3, 5, 4, 2, 8, 3, 7]), 5)
    
    def test_no_peak(self):
        self.assertEqual(longest_peak([1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)
        self.assertEqual(longest_peak([9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)
        self.assertEqual(longest_peak([1, 2]), 'There must be more than 3 numbers')
        self.assertEqual(longest_peak([1, 1, 1, 1, 1, 1, 1, 1]), 0)
    
    def test_three_peaks(self):
        self.assertEqual(longest_peak([1, 3, 5, 2, 4, 6, 3, 8, 10, 7, 2, 9, 11, 5]), 5)
    
if __name__ == "__main__":
    unittest.main()
    
