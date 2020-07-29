import unittest
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # edge case
        if nums[0] == 0 and len(nums) == 1:
            return 1

        current_max = 0
        result = 0
        last_zero = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
            else:
                result = max(result, current_max)
                current_max = i - last_zero
                last_zero = i

        return max(result, current_max)


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([1, 1, 0, 1, 1, 1], 6),
            ([1, 0, 1, 1, 0], 4),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.findMaxConsecutiveOnes(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
