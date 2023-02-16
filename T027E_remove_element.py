from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        # nums[:widx+1] have written
        widx = -1
        for ridx in range(len(nums)):
            if nums[ridx] != val:
                widx += 1
                # swap ridx and widx in nums
                if ridx != widx:
                    nums[ridx], nums[widx] = nums[widx], nums[ridx]

        return widx + 1
