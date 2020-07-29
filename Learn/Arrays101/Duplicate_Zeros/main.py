import unittest
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        # 複製される0の数を求める
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            # 変更後のリストに含まれる最後の文字のindexを超えたらbreakする
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                # エッジケース: 変更後のリストの最後の数字が0になる場合は複製しない、arrayのspaceがないため
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        # 変更後のリストに含まれる最後の要素から始める
        last = length_ - possible_dups
        print(f'last={last}')

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            print(f'i={i}')
            print(f'arr[i]={arr[i]}')
            print(f'possible_dups={possible_dups}')
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        test_patterns = [
            ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                self.sol.duplicateZeros(param1)
                self.assertEqual(expected, param1)


if __name__ == "__main__":
    unittest.main()
