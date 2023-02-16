from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)

        if l1 > l2:
            l1, l2 = l2, l1
            nums1, nums2 = nums2, nums1

        if l2 == 0:
            return 0.0

        if l1 == 0:
            if l2 & 1 == 1:
                return nums2[l2 // 2]  # odd
            return (nums2[l2 // 2 - 1] + nums2[l2 // 2]) / 2.0

        half = (l1 + l2) // 2
        beg, end = 0, l1
        while beg < end:
            # nums1[:i] | nums1[i:]
            # nums2[:j] | nums2[j:]
            #   len(nums1[:i]) + len(nums2[:j]) == half
            #   len(nums1[i:]) + len(nums2[j:]) == half if even else half+1
            i = (beg + end) // 2
            j = half - i
            if nums1[i] < nums2[j - 1]:
                beg = i + 1
            else:
                end = i

        if (l1 + l2) & 1 == 1:  # odd
            # min of right part
            if end == l1:
                return nums2[half - end]
            return min(nums1[end], nums2[half - end])

        # max of left part
        if end == 0:
            r1 = nums2[half - 1]
        elif end == l1 and l1 == l2:
            r1 = nums1[l1 - 1]
        else:
            r1 = max(nums1[end - 1], nums2[half - end - 1])

        # min of right part
        if end == l1:
            r2 = nums2[half - l1]
        elif end == 0 and l1 == l2:
            r2 = nums1[0]
        else:
            r2 = min(nums1[end], nums2[half - end])

        return (r1 + r2) / 2.0
