import sys
import os
import unittest

sys.path.append(os.path.abspath(r"C:\PROGRAMMING\Second_course\Programming-Ivaskiv\Lab8\src"))

from main import read_file, build_graph, edmonds_karp

class TestGraph(unittest.TestCase):
    def test_flow(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'map.csv')
        file_path = os.path.abspath(file_path)  
        farms, shops, roads = read_file(file_path)
        graph, src, sink = build_graph(farms, shops, roads)
        result = edmonds_karp(graph, src, sink)
        self.assertEqual(result, 49)  


if __name__ == "__main__":
    unittest.main()
