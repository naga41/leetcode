from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        need_change_num = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                need_change_num += 1
        return need_change_num


if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3]
    sol = Solution()
    print(heights)
    print(sol.heightChecker(heights))

    heights = [5, 1, 2, 3, 4]
    print(heights)
    print(sol.heightChecker(heights))

    heights = [1, 2, 3, 4, 5]
    print(heights)
    print(sol.heightChecker(heights))

    heights = [2, 1]
    print(heights)
    print(sol.heightChecker(heights))

    heights = [1]
    print(heights)
    print(sol.heightChecker(heights))

    heights = []
    print(heights)
    print(sol.heightChecker(heights))
