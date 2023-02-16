from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for idx, num in enumerate(nums):
            if num in cache:
                return [cache[num], idx]
            cache[target - num] = idx
        return []
