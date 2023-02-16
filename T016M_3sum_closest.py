from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        min_sum = nums[0] + nums[1] + nums[2]
        min_dist = abs(target - min_sum)

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                dist = abs(target - s)
                if dist == 0:
                    return target
                if dist < min_dist:
                    min_sum = s
                    min_dist = dist
                if s > target:
                    k -= 1
                else:
                    j += 1

        return min_sum
