#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  bool match(char *s, int sl, char *p, int pl) {
    if (!pl)
      return !sl;
    char c = p[0];
    if (pl > 1 && p[1] == '*') {
      if (sl > 0 && (c == '.' || s[0] == c))
        return match(s, sl, p + 2, pl - 2) || match(s + 1, sl - 1, p, pl);
      return match(s, sl, p + 2, pl - 2);
    }
    if (sl == 0 || (c != '.' && s[0] != c))
      return false;
    return match(s + 1, sl - 1, p + 1, pl - 1);
  }

  bool isMatch_rec(string s, string p) {
    return match(&s[0], s.length(), &p[0], p.length());
  }

  bool match_cached(char *s, int sl, char *p, int pl, vector<vector<pair<bool, bool>>> &cache) {
    if (cache[sl][pl].first)
      return cache[sl][pl].second;
    cache[sl][pl].first = true;
    if (!pl)
      return cache[sl][pl].second = !sl;
    char c = p[0];
    if (pl > 1 && p[1] == '*') {
      if (sl > 0 && (c == '.' || s[0] == c))
        return cache[sl][pl].second =
          match_cached(s, sl, p + 2, pl - 2, cache) ||
          match_cached(s + 1, sl - 1, p, pl, cache);
      return cache[sl][pl].second =
        match_cached(s, sl, p + 2, pl - 2, cache);
    }
    if (sl == 0 || (c != '.' && s[0] != c))
      return cache[sl][pl].second = false;
    return cache[sl][pl].second = match_cached(s + 1, sl - 1, p + 1, pl - 1, cache);
  }

  bool isMatch_rec_cached(string s, string p) {
    vector<vector<pair<bool, bool>>> cache(s.length() + 1, vector<pair<bool, bool>>(p.length() + 1));
    return match_cached(&s[0], s.length(), &p[0], p.length(), cache);
  }

  bool isMatch_dp(string s, string p) {
    int sl = s.length(), pl = p.length();
    vector<vector<bool>> dp (sl + 1, vector<bool>(pl + 1));
    dp[0][0] = true;
    dp[0][1] = false;
    for (int i = 2; i < pl + 1; i++)
      dp[0][i] = dp[0][i - 2] && p[i - 1] == '*';
    for (int i = 1; i < sl + 1; i++)
      dp[i][0] = false;
    for (int i = 1; i < pl + 1; i++)
      for (int j = 1; j < sl + 1; j++)
        if (p[i - 1] == '*')
          dp[j][i] = dp[j][i - 2] || (dp[j - 1][i] && (p[i - 2] == '.' || p[i - 2] == s[j - 1]));
        else
          dp[j][i] = dp[j - 1][i - 1] && (p[i - 1] == '.' || p[i - 1] == s[j - 1]);
    return dp[sl][pl];
  }

  bool isMatch(string s, string p) {
    return isMatch_rec_cached(s, p);
  }
};
