import unittest
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            pass
        else:
            write_pointer = 0
            for read_pointer in range(len(A)):
                if A[read_pointer] % 2 == 0:
                    A[read_pointer], A[write_pointer] = \
                        A[write_pointer], A[read_pointer]
                    write_pointer += 1
        return A


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([0, 1, 0, 3, 12], [0, 0, 12, 3, 1]),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 0],
                [0, 0, 2, 2, 4, 0, 1, 3, 3, 1, 1]),
            ([3, 1, 2, 4], [2, 4, 3, 1]),
            ([1, 2], [2, 1]),
            ([1], [1]),
            ([], []),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.sortArrayByParity(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
