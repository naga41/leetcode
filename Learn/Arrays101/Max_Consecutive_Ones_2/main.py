from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # edge case
        if nums[0] == 0 and len(nums) == 1:
            return 1

        current_max = 0
        result = 0
        last_zero = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
            else:
                result = max(result, current_max)
                current_max = i - last_zero
                last_zero = i

        return max(result, current_max)


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums))

    nums = [1, 0, 1, 1, 0]
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums))
