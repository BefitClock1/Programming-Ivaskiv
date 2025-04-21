from Lab5_main import count_islands 
import unittest

class test(unittest.TestCase):
      def first_test(self):
            matrix = [
                  1, 1, 1, 0, 0, 1,
                  1, 1, 0, 0, 0, 1,
                  1, 0, 0, 0, 0, 0,
                  0, 0, 1, 1, 1, 0,
            ]
            self.assertEqual(count_islands(matrix), 3)
      
      def Second_test(self):
            matrix = [
                  1, 1,
                  1, 1
            ]
            self.assertEqual(count_islands(matrix), 1)

      def first_test(self):
            matrix = [
                  0, 0,
                  0, 0
            ]
            self.assertEqual(count_islands(matrix), 0)