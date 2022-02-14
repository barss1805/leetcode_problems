from unittest import TestCase, main
from ..task_13 import Solution


class SolutionTest(TestCase):
    sol = Solution()

    def test_one_letter_D(self):
        self.assertEqual(self.sol.roman_to_int("D"), 500)

    def test_one_letter_M(self):
        self.assertEqual(self.sol.roman_to_int("M"), 1000)

    def test_some_letters_LVIII(self):
        self.assertEqual(self.sol.roman_to_int("LVIII"), 58)

    def test_some_letters_MCMXCIV(self):
        self.assertEqual(self.sol.roman_to_int("MCMXCIV"), 1994)

    def test_no_digits_in_str_1(self):
        with self.assertRaises(KeyError) as e:
            self.sol.roman_to_int("MCM1")
        self.assertEqual("1", e.exception.args[0])

    def test_no_empty_in_str(self):
        with self.assertRaises(KeyError) as e:
            self.sol.roman_to_int("MCM XCIV")
        self.assertEqual(" ", e.exception.args[0])


if __name__ == '__main__':
    main()
