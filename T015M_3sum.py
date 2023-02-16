from typing import List, Set


def uniq(nums: List[int]) -> List[int]:
    # same numbers at most 2
    nums_uniq = []
    i = 0
    while i < len(nums):
        num = nums[i]
        nums_uniq.append(num)
        if i + 1 < len(nums) and nums[i + 1] == num:
            nums_uniq.append(num)
            while i < len(nums) and nums[i] == num:
                i += 1
        else:
            i += 1
    return nums_uniq


def twoSum(nums: List[int], targets: Set[int], res: List[List[int]]):
    i = 0
    while i < len(nums):
        num1 = nums[i]
        j = i + 1
        while j < len(nums):
            num2 = nums[j]
            num = num1 + num2
            if -num in targets:
                res.append([num1, num2, -num])
            # skip dup numbers
            if j + 1 < len(nums) and nums[j + 1] == num2:
                j += 2
            else:
                j += 1
        # skip dup numbers
        if i + 1 < len(nums) and nums[i + 1] == num1:
            i += 2
        else:
            i += 1


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        zeros = nums.count(0)
        nums1 = sorted(num for num in nums if num < 0)
        nums2 = sorted(num for num in nums if num > 0)

        if len(nums1) > len(nums2):  # ensure len(nums1) <= len(nums2)
            nums1, nums2 = nums2, nums1

        nums1_uniq = uniq(nums1)
        nums2_uniq = uniq(nums2)

        nums1_set = set(nums1_uniq)
        nums2_set = set(nums2_uniq)

        if zeros >= 3:
            res.append([0, 0, 0])

        if zeros >= 1:
            for num in nums1_set:
                if -num in nums2_set:
                    res.append([-num, 0, num])

        twoSum(nums1_uniq, nums2_set, res)
        twoSum(nums2_uniq, nums1_set, res)

        return res
