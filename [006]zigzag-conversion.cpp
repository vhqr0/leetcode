#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  string convert(string s, int numRows) {
    if (numRows < 2)
      return s;
    vector<string> v(numRows, "");
    int bs = (numRows - 1) * 2;
    for (int i = 0; i < s.length(); i++) {
      int j = i % bs;
      if (j < numRows)
        v[j] += s[i];
      else
        v[bs - j] += s[i];
    }
    string r = "";
    for (auto str : v)
      r += str;
    return r;
  }
};
