import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([3, 2, 2, 3], 3, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ]

        for param1, param2, expected in test_patterns:
            with self.subTest(param1=param1, param2=param2):
                actual = self.sol.removeElement(param1, param2)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
