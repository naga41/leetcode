from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                consecutive_ones = max(consecutive_ones, count)
                count = 0
        return max(consecutive_ones, count)


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums))
