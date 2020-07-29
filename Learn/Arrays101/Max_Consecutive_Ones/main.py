import unittest
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                consecutive_ones = max(consecutive_ones, count)
                count = 0
        return max(consecutive_ones, count)


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([1, 1, 0, 1, 1, 1], 3),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.findMaxConsecutiveOnes(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
