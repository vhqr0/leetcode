from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        beg, end = 0, len(height) - 1

        while beg < end:
            area = min(height[beg], height[end]) * (end - beg)
            if area > max_area:
                max_area = area
            if height[beg] < height[end]:
                h = height[beg]
                beg += 1
                while beg < end and height[beg] <= h:
                    beg += 1
            else:
                h = height[end]
                end -= 1
                while beg < end and height[end] <= h:
                    end -= 1

        return max_area
