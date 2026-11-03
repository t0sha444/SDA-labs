import unittest
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path, module_name):
    path = ROOT / relative_path
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestLab4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quick = load_module("algorithms/quicksort.py", "lab4_quicksort")
        cls.search = load_module("algorithms/binary_search.py", "lab4_search")
        cls.merge_sort_module = load_module(
            "lab3/solutions/912_sort_an_array.py", "lab3_merge_sort"
        )

    def test_partition_first_pivot(self):
        values = [6, 2, 5, 2, 1]
        pivot_index = self.quick.partition(values, 0, len(values))
        pivot = values[pivot_index]
        self.assertEqual(pivot, 6)
        self.assertEqual(values, [1, 2, 5, 2, 6])
        self.assertTrue(all(value < pivot for value in values[:pivot_index]))
        self.assertTrue(all(value >= pivot for value in values[pivot_index + 1:]))

    def test_quicksort_required_cases(self):
        cases = [
            [],
            [7],
            [-3, 5, -1, 0, -8],
            [3, 1, 3, 2, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 2, 2, 2, 2],
            [6, 2, 5, 2, 1],
        ]
        for original in cases:
            with self.subTest(original=original):
                values = original.copy()
                result = self.quick.quicksort(values)
                self.assertIs(result, values)
                self.assertEqual(values, sorted(original))
                self.assertEqual(Counter(values), Counter(original))

    def test_quicksort_matches_lab3_merge_sort(self):
        merge_solution = self.merge_sort_module.Solution()
        cases = [
            [6, 2, 5, 2, 1],
            [-10, 4, 0, -10, 3, 2],
            [1, 2, 3, 4, 5],
            [9, 9, 9, 9],
        ]
        for original in cases:
            quick_values = original.copy()
            merge_values = original.copy()
            self.quick.quicksort(quick_values)
            merge_solution.sortArray(merge_values)
            self.assertEqual(quick_values, merge_values)

    def test_binary_search(self):
        values = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(self.search.binary_search(values, 9), 4)
        self.assertEqual(self.search.binary_search(values, 2), -1)
        self.assertEqual(self.search.binary_search(values, -1), 0)
        self.assertEqual(self.search.binary_search(values, 12), 5)
        self.assertEqual(self.search.binary_search([8], 8), 0)
        self.assertEqual(self.search.binary_search([8], 3), -1)
        self.assertEqual(self.search.binary_search(values, -5), -1)
        self.assertEqual(self.search.binary_search(values, 20), -1)
        self.assertEqual(self.search.binary_search(values, 4), -1)
        self.assertEqual(self.search.binary_search([], 1), -1)

    def test_search_insert_position(self):
        values = [1, 3, 5, 6]
        self.assertEqual(self.search.search_insert_position(values, 5), 2)
        self.assertEqual(self.search.search_insert_position(values, 2), 1)
        self.assertEqual(self.search.search_insert_position(values, 0), 0)
        self.assertEqual(self.search.search_insert_position(values, 7), 4)
        self.assertEqual(self.search.search_insert_position([8], 3), 0)
        self.assertEqual(self.search.search_insert_position([], 3), 0)


if __name__ == "__main__":
    unittest.main()
