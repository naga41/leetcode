import unittest
from main import Solution


class TestCheckIfExist(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_check_if_exist(self):
        test_patterns = [
            ([10, 2, 5, 3], True),
            ([7, 1, 14, 11], True),
            ([3, 1, 7, 11], False),
            ([], False),
            ([0], False),
            ([2, 4, 6], True),
            ([-2, 0, 10, -19, 4, 6, -8], False),
            ([0, 0], True),
        ]

        for param1, expected in test_patterns:
            with self.subTest(param1=param1):
                actual = self.sol.checkIfExist(param1)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
