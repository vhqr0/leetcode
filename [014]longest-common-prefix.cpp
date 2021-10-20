#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  string longestCommonPrefix(vector<string> &strs) {
    if (strs.empty())
      return "";
    int prefix = 0;
    for (;;) {
      if (strs[0].length() == prefix)
        break;
      char c = strs[0][prefix];
      for (int i = 1; i < strs.size(); i++)
        if (strs[i][prefix] != c)
          goto exit;
      prefix++;
    }
  exit:
    return strs[0].substr(0, prefix);
  }
};
