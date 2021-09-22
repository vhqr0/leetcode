#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
    int s1 = nums1.size(), s2 = nums2.size();
    if (!s1 && !s2)
      return 0;
    if (!s1) {
      if (s2 & 1)
        return nums2[s2 / 2];
      return (nums2[s2 / 2 - 1] + nums2[s2 / 2]) / 2.0;
    }
    if (!s2) {
      if (s1 & 1)
        return nums1[s1 / 2];
      return (nums1[s1 / 2 - 1] + nums1[s1 / 2]) / 2.0;
    }
    int *n1, *n2;
    if (s1 > s2) {
      swap(s1, s2);
      n1 = &nums2[0];
      n2 = &nums1[0];
    } else {
      n1 = &nums1[0];
      n2 = &nums2[0];
    }
    int t = (s1 + s2) / 2;
    int beg = 0, end = s1;
    while (beg < end) {
      int i = (beg + end) / 2;
      int j = t - i;
      if (n1[i] < n2[j - 1])
        beg = i + 1;
      else 
        end = i;
    }
    if ((s1 + s2) & 1) {
      if (end == s1)
        return n2[t - end];
      return min(n1[end], n2[t - end]);
    }
    if (s1 == s2) {
      if (end == 0)
        return (n1[0] + n2[s2 - 1]) / 2.0;
      if (end == s1)
        return (n1[s1 - 1] + n2[0]) / 2.0;
    }
    return ((end == 0 ? n2[t - end - 1] : max(n1[end - 1], n2[t - end - 1])) +
            (end == s1 ? n2[t - end] : min(n1[end], n2[t - end]))) / 2.0;
  }
};
