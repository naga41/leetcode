from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(len(nums) - 1):
            if nums[i] != nums[j + 1]:
                i += 1
                nums[i] = nums[j + 1]
        return i + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(nums)

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.removeDuplicates(nums))
    print(nums)
