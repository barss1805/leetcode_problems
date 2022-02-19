# Runtime: 768 ms, faster than 74.78% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.4 MB, less than 70.91% of Python3 online submissions for Container With Most Water.

class Solution:
    def max_area(self, height: list[int]) -> int:
        # set index first element array
        index_start = 0
        # get index last element in array
        index_end = len(height)-1
        out = 0
        while index_start < index_end:
            # get min height between elements
            min_height = min(height[index_start], height[index_end])
            # calculate area
            area = min_height * (index_end - index_start)
            # set bigger value to variable
            out = max(area, out)
            # shorten the array depending on the smaller value
            if height[index_start] < height[index_end]:
                index_start += 1
            else:
                index_end -= 1
        return out


if __name__ == '__main__':
    pass