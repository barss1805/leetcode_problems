class Solution:
    def trap(self, height: list[int]) -> int:
        lenght = len(height)
        arr_height = max(height)
        tmp_arr = []
        for _ in range(arr_height):
            inner_arr = []
            for indx, value in enumerate(height):
                if value > 0:
                    height[indx] -= 1
                    inner_arr.append(1)
                else:
                    inner_arr.append(0)
            tmp_arr.append(inner_arr)

        for j in tmp_arr:
            print(j)


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
