# Runtime: 60 ms, faster than 89.45% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 59.18% of Python3 online submissions for Two Sum.

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        out_d = {}
        for indx, value in enumerate(nums):
            if target - value in out_d:
                return [out_d[target - value], indx]
            out_d[value] = indx


if __name__ == "__main__":
    pass
