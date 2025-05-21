import unittest
from target_sum import find_two_sum

class TestFindTwoSum(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(find_two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_multiple_options(self):
        nums = [1, 3, 4, 2, 6]
        target = 5
        result = find_two_sum(nums, target)
        # Verifica que los índices sean diferentes y que la suma dé el target
        self.assertNotEqual(result[0], result[1])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_no_solution(self):
        self.assertEqual(find_two_sum([1, 2, 3], 10), [])

    def test_negative_numbers(self):
        self.assertEqual(find_two_sum([-3, 4, 3, 90], 0), [0, 2])

    def test_empty_list(self):
        self.assertEqual(find_two_sum([], 5), [])

    def test_single_element(self):
        self.assertEqual(find_two_sum([5], 5), [])

if __name__ == '__main__':
    unittest.main()