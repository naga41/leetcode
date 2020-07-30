import unittest
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        # make unique
        write_pointer = 0
        for read_pointer in range(len(sorted_nums)):
            if sorted_nums[write_pointer] != sorted_nums[read_pointer]:
                write_pointer += 1
                sorted_nums[write_pointer] = sorted_nums[read_pointer]

        if len(nums) >= 3:
            return sorted_nums[write_pointer - 2]
        else:
            return sorted_nums[-1]


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([3, 2, 1], 1),
            ([1, 2], 2),
            ([2, 2, 3, 1], 1),
            ([2, 2, 3, 1, 4, 5, 5, 10], 4),
            ([1], 1)
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.thirdMax(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
