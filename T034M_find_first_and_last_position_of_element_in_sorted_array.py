from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)

        # 11223344
        #   _i
        #    _j
        # nums[i] >= 2 and nums[i-1] < 2
        # nums[j] <= 2 and nums[j+1] > 2

        i, beg, end = 0, 0, ln
        while beg < end:
            i = (beg + end) // 2
            if i == 0:
                if nums[i] >= target:
                    break
                beg = i + 1
                continue
            a, b = nums[i - 1], nums[i]
            if a < target and b >= target:
                break
            if a < target and b < target:
                beg = i + 1
            else:
                end = i

        if i >= ln or nums[i] != target:
            return [-1, -1]

        j, beg, end = 0, 0, ln
        while beg < end:
            j = (beg + end) // 2
            if j + 1 == ln:
                if nums[j] <= target:
                    break
                end = j
                continue
            a, b = nums[j], nums[j + 1]
            if a <= target and b > target:
                break
            if a <= target and b <= target:
                beg = j + 1
            else:
                end = j

        return [i, j]
