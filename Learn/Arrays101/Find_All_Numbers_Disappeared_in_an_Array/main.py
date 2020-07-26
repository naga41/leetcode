from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_hash = {}
        for num in nums:
            nums_hash[num] = 1

        dissappeared_nums = []
        for i in range(1, len(nums) + 1):
            if i not in nums_hash:
                dissappeared_nums.append(i)

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

    nums = [10, 2, 5, 10, 9, 1, 1, 4, 3, 7]
    print(nums)
    print(sol.findDisappearedNumbers(nums))
