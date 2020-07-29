import unittest
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 0:
            return arr

        max_num = 0
        max_index = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break

            if i >= max_index:
                j = i + 1
                max_num = arr[j]
                while j < len(arr) - 1:
                    if max_num < arr[j + 1]:
                        max_num = arr[j + 1]
                        max_index = j + 1
                    j += 1
            arr[i] = max_num

        return arr


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
            ([3, 5, 5], [5, 5, -1]),
            ([0, 3, 2, 1], [3, 2, 1, -1]),
            ([1, 2, 3, 4], [4, 4, 4, -1]),
            ([0, 1, 2, 4, 2, 1], [4, 4, 4, 2, 1, -1]),
            ([0, 0], [0, -1]),
            ([0], [-1]),
            ([], []),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.replaceElements(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
