#include <string>

using namespace std;

#define MAX ((1 << 30) - 1 + (1 << 30))
#define MIN (- (1 << 30) - (1 << 30))

class Solution {
public:
  int myAtoi(string s) {
    int i;
    for (i = 0; i < s.length() && s[i] == ' '; i++);
    if (i == s.length())
      return 0;
    bool flag = s[i] == '-';
    if (flag || s[i] == '+')
      i++;
    if (s[i] < '0' || s[i] > '9')
      return 0;
    int r = 0;
    for (; i < s.length() && s[i] >= '0' && s[i] <= '9'; i++) {
      int t = s[i] - '0';
      if (flag) {
        if (r < MIN / 10 || (r == MIN / 10 && t > 8))
          return MIN;
        r = r * 10 - t;
      } else {
        if (r > MAX / 10 || (r == MAX / 10 && t > 7))
          return MAX;
        r = r * 10 + t;
      }
    }
    return r;
  }
};
