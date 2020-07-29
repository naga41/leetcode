import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # uniqueな数字の数を数える
        unique_nums = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                unique_nums += 1

        # uniqueな数字の数だけ上書きする
        unique_index = 0
        for i in range(len(nums)):
            if unique_index > unique_nums:
                break

            if i == 0 or nums[i] != nums[unique_index - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_nums


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([1, 1, 2], 2),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.removeDuplicates(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
