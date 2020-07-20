from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False

        mountain_flag = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                if mountain_flag == 1 or (i + 1) == (len(A) - 1):
                    return False
            elif A[i] > A[i + 1]:
                mountain_flag = 1
                if mountain_flag == 0 or i == 0:
                    return False
            else:
                return False

        return True


if __name__ == "__main__":
    nums = [2, 1]
    sol = Solution()
    print(sol.validMountainArray(nums))

    nums = [3, 5, 5]
    print(sol.validMountainArray(nums))

    nums = [0, 3, 2, 1]
    print(sol.validMountainArray(nums))

    nums = [1, 2, 3, 4]
    print(sol.validMountainArray(nums))

    nums = [0, 1, 2, 4, 2, 1]
    print(sol.validMountainArray(nums))

    nums = [0, 0]
    print(sol.validMountainArray(nums))

    nums = [0]
    print(sol.validMountainArray(nums))
