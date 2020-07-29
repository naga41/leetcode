import unittest
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_nums = map(str, nums)
        even_num_count = 0
        for str_num in str_nums:
            if len(str_num) % 2 == 0:
                even_num_count += 1
        return even_num_count


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([12, 345, 2, 6, 7896], 2),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.findNumbers(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
