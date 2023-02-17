import bisect

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        ln = len(nums)

        # 456123
        #   _i-1
        #    _i

        i, beg, end = 1, 1, ln
        while beg < end:
            i = (beg + end) // 2
            a, b = nums[i - 1], nums[i]
            if a >= nums[0] and b < nums[0]:
                break
            if a >= nums[0] and b >= nums[0]:
                beg = i + 1
            else:
                end = i

        # binary search in nums[:i] and nums[i:]
        pos = bisect.bisect_left(nums, target, hi=i)

        if pos == i or nums[pos] != target:
            pos = bisect.bisect_left(nums, target, lo=i)
            if pos == len(nums) or nums[pos] != target:
                return -1
            return pos

        return pos
