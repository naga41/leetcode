from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # uniqueな数字の数を数える
        unique_nums = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                unique_nums += 1

        # uniqueな数字の数だけ上書きする
        unique_index = 0
        for i in range(len(nums)):
            if unique_index > unique_nums:
                break

            if i == 0 or nums[i] != nums[unique_index - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_nums


if __name__ == "__main__":
    nums = [1, 1, 2]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(nums)

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.removeDuplicates(nums))
    print(nums)
