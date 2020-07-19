from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        if len(arr) == 0 or len(arr) == 1:
            return False

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                    return True

        return False


if __name__ == "__main__":
    nums = [10, 2, 5, 3]
    sol = Solution()
    print(sol.checkIfExist(nums))

    nums = [7, 1, 14, 11]
    print(sol.checkIfExist(nums))

    nums = [3, 1, 7, 11]
    print(sol.checkIfExist(nums))

    nums = []
    print(sol.checkIfExist(nums))

    nums = [0]
    print(sol.checkIfExist(nums))

    nums = [2, 4, 6]
    print(sol.checkIfExist(nums))

    nums = [-2, 0, 10, -19, 4, 6, -8]
    print(sol.checkIfExist(nums))

    nums = [0, 0]
    print(sol.checkIfExist(nums))
