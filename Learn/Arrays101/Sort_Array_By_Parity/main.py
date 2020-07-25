from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            pass
        else:
            write_pointer = 0
            for read_pointer in range(len(A)):
                if A[read_pointer] % 2 == 0:
                    A[read_pointer], A[write_pointer] = \
                        A[write_pointer], A[read_pointer]
                    write_pointer += 1
        return A


if __name__ == "__main__":
    A = [0, 1, 0, 3, 12]
    sol = Solution()
    print(sol.sortArrayByParity(A))
    print(A)

    A = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 0]
    print(sol.sortArrayByParity(A))
    print(A)

    A = [3, 1, 2, 4]
    print(sol.sortArrayByParity(A))
    print(A)

    A = [1, 2]
    print(sol.sortArrayByParity(A))
    print(A)

    A = [1]
    print(sol.sortArrayByParity(A))
    print(A)

    A = []
    print(sol.sortArrayByParity(A))
    print(A)
