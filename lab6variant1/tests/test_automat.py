import unittest
from src.main import automat, build_suffix_arr

class TestAutomaton(unittest.TestCase):

    def test_build_suffix_arr(self):
        needle = "abc"
        result = build_suffix_arr(needle)
        expected = [0, 1, 2]
        self.assertEqual(result, expected)

    def test_automat(self):
        haystack = "abbccabbcbabc"
        needle = "abc"
        result = automat(haystack, needle)
        expected = [10]
        self.assertEqual(result, expected)

    # Додайте інші тести за необхідності

if __name__ == '__main__':
    unittest.main()

