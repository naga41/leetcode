import unittest
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_hash = {}
        for num in nums:
            nums_hash[num] = 1

        dissappeared_nums = []
        for i in range(1, len(nums) + 1):
            if i not in nums_hash:
                dissappeared_nums.append(i)

        return dissappeared_nums


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([3, 2, 1], []),
            ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
            ([2, 2, 3, 1], [4]),
            ([2, 2, 3, 1, 4, 5, 5, 8], [6, 7]),
            ([1], []),
            ([10, 2, 5, 10, 9, 1, 1, 4, 3, 7], [6, 8]),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.findDisappearedNumbers(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
