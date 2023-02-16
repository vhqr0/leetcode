from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:widx+1] have written
        widx = 0
        for ridx in range(1, len(nums)):
            if nums[ridx] > nums[widx]:
                widx += 1
                # swap ridx and widx in nums
                if ridx != widx:
                    nums[ridx], nums[widx] = nums[widx], nums[ridx]

        return widx + 1
