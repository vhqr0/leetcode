#define MAX ((1 << 30) - 1 + (1 << 30))
#define MIN (- (1 << 30) - (1 << 30))

class Solution {
public:
  int reverse(int x) {
    bool flag = x < 0;
    int r = 0;
    for (; x; x /= 10) {
      if (flag) {
        if (r < MIN / 10)
          return 0;
      } else {
        if (r > MAX / 10)
          return 0;
      }
      r = r * 10 + x % 10;
    }
    return r;
  }
};
