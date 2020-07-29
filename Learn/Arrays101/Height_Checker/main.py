import unittest
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        need_change_num = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                need_change_num += 1
        return need_change_num


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([1, 1, 4, 2, 1, 3], 3),
            ([5, 1, 2, 3, 4], 5),
            ([1, 2, 3, 4, 5], 0),
            ([2, 1], 2),
            ([1], 0),
            ([], 0),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.heightChecker(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
