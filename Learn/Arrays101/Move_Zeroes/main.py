from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            pass
        else:
            write_pointer = 0
            for read_pointer in range(len(nums)):
                if nums[read_pointer] != 0:
                    nums[write_pointer] = nums[read_pointer]
                    write_pointer += 1
            while write_pointer < len(nums):
                nums[write_pointer] = 0
                write_pointer += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    print(sol.moveZeroes(nums))
    print(nums)

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 0]
    print(sol.moveZeroes(nums))
    print(nums)

    nums = [0]
    print(sol.moveZeroes(nums))
    print(nums)

    nums = []
    print(sol.moveZeroes(nums))
    print(nums)
