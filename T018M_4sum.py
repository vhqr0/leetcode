from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                k, m = j + 1, len(nums) - 1

                while k < m:
                    s = nums[i] + nums[j] + nums[k] + nums[m]
                    if s > target:
                        m -= 1
                    elif s < target:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        k += 1
                        while nums[k - 1] == nums[k] and k < m:
                            k += 1
                        m -= 1
                        while nums[m] == nums[m + 1] and k < m:
                            m -= 1

        return res
