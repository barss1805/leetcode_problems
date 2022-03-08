class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        len_arr = len(strs)
        if len_arr < 2:
            return ""
        for i in range(1, len_arr, 1):
            print(strs[i])



if __name__ == '__main__':
    sol = Solution()
    sol.longest_common_prefix(["flower", "flow", "flight"])
    # sol.longest_common_prefix(["flower"])