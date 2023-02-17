from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def trans(nums: List[int], last: int) -> bool:
            if last == 1:  # cannot trans
                return False

            if trans(nums, last - 1):  # transed
                return True

            # find next small num
            candidates = [n for n in nums[-last + 1:] if n > nums[-last]]
            if not candidates:
                return False
            n = min(candidates)

            pos = nums.index(n, -last + 1)
            nums[-last], nums[pos] = nums[pos], nums[-last]
            nums[-last + 1:] = sorted(nums[-last + 1:])

            return True

        if not trans(nums, len(nums)):
            nums.sort()
