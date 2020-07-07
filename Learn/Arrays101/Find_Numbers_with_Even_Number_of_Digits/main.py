from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_nums = map(str, nums)
        even_num_count = 0
        for str_num in str_nums:
            if len(str_num) % 2 == 0:
                even_num_count += 1
        return even_num_count


if __name__ == '__main__':
    nums = [12, 345, 2, 6, 7896]
    sol = Solution()
    print(sol.findNumbers(nums))
