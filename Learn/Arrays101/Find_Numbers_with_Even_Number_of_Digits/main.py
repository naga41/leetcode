from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_num_count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_num_count += 1
        return even_num_count


if __name__ == '__main__':
    nums = [12, 345, 2, 6, 7896]
    sol = Solution()
    print(sol.findNumbers(nums))
