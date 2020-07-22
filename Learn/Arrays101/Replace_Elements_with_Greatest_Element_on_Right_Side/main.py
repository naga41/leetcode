from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 0:
            return arr

        max_num = 0
        max_index = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break

            if i >= max_index:
                j = i + 1
                max_num = arr[j]
                while j < len(arr) - 1:
                    if max_num < arr[j + 1]:
                        max_num = arr[j + 1]
                        max_index = j + 1
                    j += 1
            arr[i] = max_num

        return arr


if __name__ == "__main__":
    arr = [17, 18, 5, 4, 6, 1]
    sol = Solution()
    print(sol.replaceElements(arr))

    arr = [3, 5, 5]
    print(sol.replaceElements(arr))

    arr = [0, 3, 2, 1]
    print(sol.replaceElements(arr))

    arr = [1, 2, 3, 4]
    print(sol.replaceElements(arr))

    arr = [0, 1, 2, 4, 2, 1]
    print(sol.replaceElements(arr))

    arr = [0, 0]
    print(sol.replaceElements(arr))

    arr = [0]
    print(sol.replaceElements(arr))

    arr = []
    print(sol.replaceElements(arr))
