#define MAX ((1 << 30) - 1 + (1 << 30))
#define MIN (- (1 << 30) - (1 << 30))

class Solution {
public:
  bool ip_rec(int x) {
    if (x < 0)
      return false;
    int r = 0;
    for (int t = x; t; t /= 10) {
      if (r > MAX / 10)
        return false;
      r = r * 10 + t % 10;
    }
    return r == x;
  }

  bool ip_rec_half(int x) {
    if (x < 0 || (!(x % 10) && x))
      return false;
    int r = 0;
    while (x > r) {
      r = r * 10 + x % 10;
      x /= 10;
    }
    return x == r || x == r / 10;
  }

  bool isPalindrome(int x) {
    return ip_rec_half(x);
  }
};
