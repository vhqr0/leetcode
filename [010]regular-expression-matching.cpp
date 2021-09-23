#include <string>

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
    if (sl == 0 || ((c != '.') && (s[0] != c)))
      return false;
    return match(s + 1, sl - 1, p + 1, pl - 1);
  }

  bool isMatch(string s, string p) {
    int sl = s.length(), pl = p.length();
    return match(&s[0], sl, &p[0], pl);
  }
};
