import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(len(nums) - 1):
            if nums[i] != nums[j + 1]:
                i += 1
                nums[i] = nums[j + 1]
        return i + 1


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
