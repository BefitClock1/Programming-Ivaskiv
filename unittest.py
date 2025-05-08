from Lab6_main import find_unreachable_cities
import unittest
class TestGasPipeline(unittest.TestCase):
    def test_all_reachable(self):
        storages = ['Сховище_1', 'Сховище_2']
        cities = ['Львів', 'Стрий', 'Долина']
        pipelines = [
            ['Львів', 'Стрий'],
            ['Долина', 'Львів'],
            ['Сховище_1', 'Сховище_2'],
            ['Сховище_2', 'Долина']
        ]
        self.assertEqual(find_unreachable_cities(storages, cities, pipelines), [])

    def test_some_unreachable(self):
        storages = ['Сховище_1']
        cities = ['Львів', 'Стрий', 'Долина']
        pipelines = [
            ['Сховище_1', 'Долина']
        ]
        self.assertEqual(find_unreachable_cities(storages, cities, pipelines),
                         [['Сховище_1', ['Львів', 'Стрий']]])

    def test_none_reachable(self):
        storages = ['Сховище_1']
        cities = ['Львів', 'Стрий']
        pipelines = []
        self.assertEqual(find_unreachable_cities(storages, cities, pipelines),
                         [['Сховище_1', ['Львів', 'Стрий']]])

if __name__ == '__main__':
    unittest.main()