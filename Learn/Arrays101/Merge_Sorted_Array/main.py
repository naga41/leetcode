import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums2をすべて評価するまでループ
        while n > 0:
            # merge先（nums1）の値を全て評価するか、nums2の値がnums1の値より大きい場合
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([1, 2, 3, 0, 0, 0, 0], 3, [2, 4, 5, 6], 4, [1, 2, 2, 3, 4, 5, 6]),
        ]

        for param1, param2, param3, param4, expected in test_patterns:
            with self.subTest(
                param1=param1, param2=param2, param3=param3, param4=param4
            ):
                self.sol.merge(param1, param2, param3, param4)
                self.assertEqual(expected, param1)


if __name__ == "__main__":
    unittest.main()
