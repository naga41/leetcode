from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        # make unique
        write_pointer = 0
        for read_pointer in range(len(sorted_nums)):
            if sorted_nums[write_pointer] != sorted_nums[read_pointer]:
                write_pointer += 1
                sorted_nums[write_pointer] = sorted_nums[read_pointer]

        if len(nums) >= 3:
            return sorted_nums[write_pointer - 2]
        else:
            return sorted_nums[-1]


if __name__ == "__main__":
    nums = [3, 2, 1]
    sol = Solution()
    print(nums)
    print(sol.thirdMax(nums))

    nums = [1, 2]
    sol = Solution()
    print(nums)
    print(sol.thirdMax(nums))

    nums = [2, 2, 3, 1]
    print(nums)
    print(sol.thirdMax(nums))

    nums = [2, 2, 3, 1, 4, 5, 5, 10]
    print(nums)
    print(sol.thirdMax(nums))

    nums = [1]
    print(nums)
    print(sol.thirdMax(nums))
