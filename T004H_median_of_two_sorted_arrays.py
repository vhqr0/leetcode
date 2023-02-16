from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)

        if l1 == 0 and l2 == 0:
            return 0.0
        if l1 == 0:
            if l2 & 1 == 1:
                return nums2[l2 // 2]  # odd
            return (nums2[l2 // 2 - 1] + nums2[l2 // 2]) / 2.0
        if l2 == 0:
            if l1 & 1 == 1:
                return nums1[l1 // 2]  # odd
            return (nums1[l1 // 2 - 1] + nums1[l1 // 2]) / 2.0

        if l1 > l2:  # ensure l1 <= l2
            l1, l2 = l2, l1
            nums1, nums2 = nums2, nums1

        t = (l1 + l2) // 2
        beg, end = 0, l1
        while beg < end:
            # nums1[:i] | nums1[i:]
            # nums2[:j] | nums2[j:]
            #   len(nums1[:i]) + len(nums2[:j]) == t
            #   len(nums1[i:]) + len(nums2[j:]) == t if even else t+1
            i = (beg + end) // 2
            j = t - i
            if nums1[i] < nums2[j - 1]:
                beg = i + 1
            else:
                end = i

        if (l1 + l2) & 1 == 1:  # odd
            # min of right part
            if end == l1:
                return nums2[t - end]
            return min(nums1[end], nums2[t - end])

        # nums2[:j] | nums2[j:]
        #   make sure both parts are nonempty in nums2
        #   case l1 == l2 and nums1 < nums2 or nums1 > nums2
        if l1 == l2:
            if end == 0:
                return (nums1[0] + nums2[l2 - 1]) / 2.0
            if end == l1:
                return (nums1[l1 - 1] + nums2[0]) / 2.0

        # max of left part
        if end == 0:
            r1 = nums2[t - end - 1]
        else:
            r1 = max(nums1[end - 1], nums2[t - end - 1])

        # min of right part
        if end == l1:
            r2 = nums2[t - end]
        else:
            r2 = min(nums1[end], nums2[t - end])

        return (r1 + r2) / 2.0
