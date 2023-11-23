import unittest
from main import read_input


class TestYourCode(unittest.TestCase):

    def setUp(self):
        # Ініціалізація даних для тестів
        self.cities = ['Львів', 'Долина', 'Івано-Франківськ']
        self.storage = ['Сховище_1', 'Сховище_2']
        self.pipelines = [['Сховище_1', 'Львів'], ['Сховище_2', 'Долина']]

    def test_read_input(self):
        # Перевірка читання вхідних даних
        input_data = "Львів,Долина,Івано-Франківськ\nСховище_1,Сховище_2\nСховище_1,Львів\nСховище_2,Долина"
        expected_output = (self.cities, self.storage, self.pipelines)
        result = read_input(input_data)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
