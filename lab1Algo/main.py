import unittest


def array_is_monotonic(array):
    growing = reducing = True

    for i in range(1, (len(array)-1)):
        if array[i] >= array[i+1]:
            reducing = False

        if array[i] <= array[i+1]:
            growing = False

    return growing or reducing


class TestArrayIsMonotone(unittest.TestCase):

    def test_growing(self):
        self.assertTrue(array_is_monotonic([1, 2, 3, 4, 5]))
        self.assertFalse(array_is_monotonic([1, 1, 2, 2, 3, 4]))

    def test_reducing(self):
        self.assertTrue(array_is_monotonic([5, 4, 3, 2, 1]))
        self.assertFalse(array_is_monotonic([5, 5, 4, 4, 2, 1]))
        # self.assertNotEquals((array_is_monotone([5, 4, 3, 2, 1])), (array_is_monotone([5, 5, 4, 3, 3, 3])))

    def test_equal_elements(self):
        self.assertTrue(array_is_monotonic([1, 2, 3, 4, 5]))
        self.assertFalse(array_is_monotonic([2, 2, 2, 2]))


if __name__ == '__main__':
    print(array_is_monotonic([1, 2, 2, 3, 4, 5]))
    unittest.main()
