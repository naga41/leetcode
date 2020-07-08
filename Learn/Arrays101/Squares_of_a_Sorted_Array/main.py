from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num ** 2 for num in A)


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    sol = Solution()
    print(sol.sortedSquares(A))
