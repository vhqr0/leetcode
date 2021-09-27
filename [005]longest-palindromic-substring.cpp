#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  string lp_search(string s) {
    int sl = s.length();
    int maxlen = 0, maxpos = 0;
    for (int i = 0; i < sl;) {
      int beg = i;
      for (i++; i < sl && s[i] == s[beg]; i++);
      int end = i;
      for (beg--; beg > -1 && end < sl && s[beg] == s[end]; beg--, end++);
      beg++;
      end--;
      int len = end - beg;
      if (len > maxlen) {
        maxlen = len;
        maxpos = beg;
      }
    }
    return s.substr(maxpos, maxlen + 1);
  }

  string lp_dp(string s) {
    int sl = s.length();
    vector<vector<bool>> dp(sl, vector<bool>(sl));
    int maxlen = 0, maxpos = 0;
    for (int i = 0; i < sl; i++) {
      for (int j = 0; j < sl - i; j++) {
        if (i == 0)
          dp[j][j] = true;
        else if (i < 3)
          dp[j][j + i] = s[j] == s[j + i];
        else
          dp[j][j + i] = s[j] == s[j + i] && dp[j + 1][j + i - 1];
        if (dp[j][j + i] && i > maxlen) {
          maxlen = i;
          maxpos = j;
        }
      }
    }
    return s.substr(maxpos, maxlen + 1);
  }

  string longestPalindrome(string s) {
    return lp_search(s);
  }
};
