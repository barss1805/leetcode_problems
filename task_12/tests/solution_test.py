from unittest import TestCase, main
from ..task_12 import Solution


class SolutionTest(TestCase):
    sol = Solution()

    def test_return_one_letter(self):
        self.assertEqual(self.sol.intToRoman(500), "D")

    def test_must_return_III(self):
        self.assertEqual(self.sol.intToRoman(3), "III")

    def test_must_return_LVIII(self):
        self.assertEqual(self.sol.intToRoman(58), "LVIII")

    def test_must_return_MCMXCIV(self):
        self.assertEqual(self.sol.intToRoman(1994), "MCMXCIV")


if __name__ == '__main__':
    main()
