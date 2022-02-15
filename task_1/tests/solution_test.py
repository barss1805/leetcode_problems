from unittest import TestCase, main
from ..task_1 import Solution


class SolutionTest(TestCase):
    sol = Solution()

    def test_target_9(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_target_6(self):
        self.assertEqual(self.sol.twoSum([3, 2, 4], 6), [1, 2])

    def test_target_6_(self):
        self.assertEqual(self.sol.twoSum([3, 3], 6), [0, 1])

if __name__ == '__main__':
    main()
