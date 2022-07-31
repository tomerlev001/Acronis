import unittest
from sorting_algorithms import merge


class TestSortingAlgorithms(unittest.TestCase):

    def test_merge_multiply_iterables_return_true(self):
        it1 = [1, 4, 9]
        it2 = [1, 2, 3]
        it3 = [1, 4, 6]

        iterator = merge(it1, it2, it3)
        result = [n for n in iterator]

        self.assertEqual([1, 1, 1, 2, 3, 4, 4, 6, 9], result)

    def test_merge_single_iterable_return_true(self):
        it1 = [1, 4, 9]

        iterator = merge(it1)
        result = [n for n in iterator]

        self.assertEqual([1, 4, 9], result)

    def test_merge_different_types_of_iterables_return_true(self):
        it1 = [1, 4, 9]
        it2 = (1, 2, 3)
        it3 = {1, 4, 6}
        it4 = (n for n in [1, 2, 3])

        iterator = merge(it1, it2, it3, it4)
        result = [n for n in iterator]

        self.assertEqual([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 6, 9], result)

    def test_merge_different_length_of_iterables_return_true(self):
        it1 = [1, 4, 9, 10]
        it2 = [1]
        it3 = [1, 2]

        iterator = merge(it1, it2, it3)
        result = [n for n in iterator]

        self.assertEqual([1, 1, 1, 2, 4, 9, 10], result)

    def test_merge_duplicate_iterables_return_true(self):
        it1 = [1, 2, 3]
        it2 = [1, 2, 3]

        iterator = merge(it1, it2)
        result = [n for n in iterator]

        self.assertEqual([1, 1, 2, 2, 3, 3], result)

    def test_merge_no_arguments_return_true(self):
        iterator = merge()
        result = [n for n in iterator]

        self.assertEqual([], result)

    def test_merge_negative_numbers_return_true(self):
        it1 = [-2, -1, 0]
        it2 = [-3, -2, -1]

        iterator = merge(it1, it2)
        result = [n for n in iterator]

        self.assertEqual([-3, -2, -2, -1, -1, 0], result)

    def test_merge_iterables_with_float_numbers_return_true(self):
        it1 = [1.1, 2.1]
        it2 = [1.2, 2.2]

        iterator = merge(it1, it2)
        result = [n for n in iterator]

        self.assertEqual([1.1, 1.2, 2.1, 2.2], result)

    def test_merge_invalid_inputs_raises_TypeError(self):
        iterator = merge(None)
        self.assertRaises(TypeError,  iterator.__next__)

        iterator = merge(2)
        self.assertRaises(TypeError, iterator.__next__)

        iterator = merge([1, 2], None)
        with self.assertRaises(TypeError):
            iterator.__next__()
            iterator.__next__()

        iterator = merge(True)
        self.assertRaises(TypeError, iterator.__next__)

    def test_merge_invalid_inputs_raises_ValueError(self):
        iterator = merge("Hello")
        self.assertRaises(ValueError, iterator.__next__)

        iterator = merge([True, False])
        self.assertRaises(ValueError, iterator.__next__)

        iterator = merge([None, None])
        self.assertRaises(ValueError, iterator.__next__)


if __name__ == '__main__':
    unittest.main()
