from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

BASE = Path(__file__).parent


def load_solution(filename, module_name):
    path = BASE / "solutions" / filename
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


class Node:
    def __init__(self, value, next_node=None):
        self.val = value
        self.next = next_node


def list_values(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def test_number_of_steps():
    solution = load_solution("1342_number_of_steps.py", "problem_1342")
    cases = {0: 0, 1: 1, 8: 4, 7: 5, 14: 6}
    for number, expected in cases.items():
        assert solution.numberOfSteps(number) == expected


def test_merge_sorted_array():
    solution = load_solution("88_merge_sorted_array.py", "problem_88")

    nums1 = [2, 5, 6, 0, 0, 0]
    solution.merge(nums1, 3, [1, 2, 4], 3)
    assert nums1 == [1, 2, 2, 4, 5, 6]

    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [1, 2, 0, 0]
    solution.merge(nums1, 2, [1, 2], 2)
    assert nums1 == [1, 1, 2, 2]

    nums1 = [0, 0, 0]
    solution.merge(nums1, 2, [0], 1)
    assert nums1 == [0, 0, 0]


def test_sort_array():
    solution = load_solution("912_sort_an_array.py", "problem_912")
    cases = [
        ([], []),
        ([1], [1]),
        ([6, 2, 5, 2, 1], [1, 2, 2, 5, 6]),
        ([-5, 3, -1, 0, -5], [-5, -5, -1, 0, 3]),
        ([5, 2, 2, 5], [2, 2, 5, 5]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([9, -2, 7], [-2, 7, 9]),
    ]

    for original, expected in cases:
        values = original.copy()
        result = solution.sortArray(values)
        assert result == expected
        assert Counter(result) == Counter(original)


def test_intersection_helper_and_reverse():
    # A small helper used to validate pointer identity for LeetCode 160.
    common = Node(8, Node(10))
    head_a = Node(3, Node(1, common))
    head_b = Node(4, Node(6, Node(7, common)))

    pointer_a = head_a
    pointer_b = head_b
    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a
    assert pointer_a is common

    no_intersection_a = Node(1, Node(2))
    no_intersection_b = Node(3)
    pointer_a = no_intersection_a
    pointer_b = no_intersection_b
    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next if pointer_a else no_intersection_b
        pointer_b = pointer_b.next if pointer_b else no_intersection_a
    assert pointer_a is None

    # Validate the same iterative pointer reversal used by the LeetCode solution.
    head = Node(1, Node(2, Node(3)))
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    assert list_values(previous) == [3, 2, 1]
    assert list_values(None) == []
    assert list_values(Node(5)) == [5]


if __name__ == "__main__":
    test_number_of_steps()
    test_merge_sorted_array()
    test_sort_array()
    test_intersection_helper_and_reverse()
    print("All Lab 3 local tests passed.")
