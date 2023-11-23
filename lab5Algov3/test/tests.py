import unittest
from src.main import read_input, bfs_gas_supply

class TestGasSupply(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.input_data = "Львів,Долина,Івано-Франківськ\nСховище_1,Сховище_2\nСховище_1,Львів\nСховище_2,Долина"
        with open("test_input.txt", "w", encoding="utf-8") as file:
            file.write(self.input_data)

    def test_read_input(self):
        cities, storage, pipelines = read_input("test_input.txt")
        self.assertEqual(cities, ['Львів', 'Долина', 'Івано-Франківськ'])
        self.assertEqual(storage, ['Сховище_1', 'Сховище_2'])
        self.assertEqual(pipelines, [['Сховище_1', 'Львів'], ['Сховище_2', 'Долина']])

    def test_bfs_gas_supply(self):
        from src.main import Graph

        test_graph = Graph()
        test_graph.add_node('Львів')
        test_graph.add_node('Долина')
        test_graph.add_node('Івано-Франківськ')
        test_graph.add_node('Сховище_1')
        test_graph.add_node('Сховище_2')
        test_graph.add_edge('Сховище_1', 'Львів')
        test_graph.add_edge('Сховище_2', 'Долина')

        # Assuming storage is a list of storage nodes
        storage = ['Сховище_1', 'Сховище_2']

        actual_result = bfs_gas_supply(test_graph.graph, storage)
        expected_result = [['Сховище_1', ['Долина', 'Івано-Франківськ']],
                           ['Сховище_2', ['Івано-Франківськ','Львів']]]

        # Sort the inner lists to ensure order-independence
        actual_result.sort(key=lambda x: x[0])
        actual_result = [[x[0], sorted(x[1])] for x in actual_result]

        expected_result.sort(key=lambda x: x[0])
        expected_result = [[x[0], sorted(x[1])] for x in expected_result]

        self.assertEqual(actual_result, expected_result)

    def tearDown(self):
        # Clean up the temporary file
        import os
        os.remove("test_input.txt")


if __name__ == '__main__':
    unittest.main()