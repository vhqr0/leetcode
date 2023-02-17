from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        ln = len(nums)

        # 12345
        #  _i-1
        #   _i
        #  nums[i-1] < target and nums[i] >= target

        i, beg, end = 0, 0, ln + 1
        while beg < end:
            i = (beg + end) // 2
            if i == 0:
                if nums[i] >= target:
                    break
                beg = i + 1
                continue
            if i == ln:
                if nums[i - 1] < target:
                    break
                end = i
                continue
            a, b = nums[i - 1], nums[i]
            if a < target and b >= target:
                break
            if a < target and b < target:
                beg = i + 1
            else:
                end = i

        return i
