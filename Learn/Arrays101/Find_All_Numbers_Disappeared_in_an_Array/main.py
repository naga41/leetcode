from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dissappeared_nums = []
        for i in range(len(nums)):
            if i + 1 not in nums:
                dissappeared_nums.append(i + 1)
        return dissappeared_nums


if __name__ == "__main__":
    nums = [3, 2, 1]
    sol = Solution()
    print(nums)
    print(sol.findDisappearedNumbers(nums))

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    sol = Solution()
    print(nums)
    print(sol.findDisappearedNumbers(nums))

    nums = [2, 2, 3, 1]
    print(nums)
    print(sol.findDisappearedNumbers(nums))

    nums = [2, 2, 3, 1, 4, 5, 5, 8]
    print(nums)
    print(sol.findDisappearedNumbers(nums))

    nums = [1]
    print(nums)
    print(sol.findDisappearedNumbers(nums))
