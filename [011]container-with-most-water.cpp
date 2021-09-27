#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  int maxArea(vector<int>& height) {
    int beg = 0, end = height.size() - 1, m = 0;
    while (beg < end) {
      int a = min(height[beg], height[end]) * (end - beg);
      if (a > m)
        m = a;
      if (height[beg] < height[end]) {
        int t = height[beg++];
        while (beg < end && height[beg] <= t)
          beg++;
      }
      else {
        int t = height[end--];
        while (beg < end && height[end] <= t)
          end--;
      }
    }
    return m;
  }
};
