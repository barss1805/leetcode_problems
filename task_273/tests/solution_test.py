from unittest import TestCase, main
from ..task_273 import Solution


class SolutionTest(TestCase):
    sol = Solution()

    def test_input_123(self):
        self.assertEqual(self.sol.number_to_words(123), "One Hundred Twenty Three")

    def test_input_12345(self):
        self.assertEqual(self.sol.number_to_words(12345),
                         "Twelve Thousand Three Hundred Forty Five")

    def test_input_1234567(self):
        self.assertEqual(self.sol.number_to_words(1234567),
                         "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")


if __name__ == '__main__':
    main()
