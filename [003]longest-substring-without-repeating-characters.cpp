#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int indexes[128] = {0};
    int beg = 0, len = 0;
    for (int end = 0; end < s.length(); end++) {
      beg = max(beg, indexes[s[end]]);
      len = max(len, end - beg + 1);
      indexes[s[end]] = end + 1;
    }
    return len;
  }
};
