from unittest import TestCase, main
from ..task_14 import Solution


class SolutionTest(TestCase):
    sol = Solution()

    def test_strs(self):
        self.assertEqual(self.sol.longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_empty(self):
        self.assertEqual(self.sol.longest_common_prefix(["dog", "racecar", "car"]), "")


if __name__ == '__main__':
    main()
