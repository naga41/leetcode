from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums2をすべて評価するまでループ
        while n > 0:
            # merge先（nums1）の値を全て評価するか、nums2の値がnums1の値より大きい場合
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 5, 6]
    n = 4
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
