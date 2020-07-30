import unittest
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num ** 2 for num in A)


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.sortedSquares(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
