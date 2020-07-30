import unittest
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False

        mountain_flag = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                if mountain_flag == 1 or (i + 1) == (len(A) - 1):
                    return False
            elif A[i] > A[i + 1]:
                mountain_flag = 1
                if mountain_flag == 0 or i == 0:
                    return False
            else:
                return False

        return True


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([2, 1], False),
            ([3, 5, 5], False),
            ([0, 3, 2, 1], True),
            ([1, 2, 3, 4], False),
            ([0, 1, 2, 4, 2, 1], True),
            ([0, 0], False),
            ([0], False)
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.validMountainArray(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
