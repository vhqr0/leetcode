#include <string>

using namespace std;

class Solution {
public:
  int romanToInt(string s) {
    int len = s.length(), cur = 0, sum = 0;
    while (cur < len) {
      switch (s[cur]) {
      case 'M':
        sum += 1000;
        cur++;
        break;
      case 'D':
        sum += 500;
        cur++;
        break;
      case 'L':
        sum += 50;
        cur++;
        break;
      case 'V':
        sum += 5;
        cur++;
        break;
      case 'C':
        if (cur + 1 < len) {
          if (s[cur + 1] == 'M') {
            sum += 900;
            cur += 2;
          } else if (s[cur + 1] == 'D') {
            sum += 400;
            cur += 2;
          } else {
            sum += 100;
            cur++;
          }
        } else {
          sum += 100;
          cur++;
        }
        break;
      case 'X':
        if (cur + 1 < len) {
          if (s[cur + 1] == 'C') {
            sum += 90;
            cur += 2;
          } else if (s[cur + 1] == 'L') {
            sum += 40;
            cur += 2;
          } else {
            sum += 10;
            cur++;
          }
        } else {
          sum += 10;
          cur++;
        }
        break;
      default:
        if (cur + 1 < len) {
          if (s[cur + 1] == 'X') {
            sum += 9;
            cur += 2;
          } else if (s[cur + 1] == 'V') {
            sum += 4;
            cur += 2;
          } else {
            sum++;
            cur++;
          }
        } else {
          sum++;
          cur++;
        }
      }
    }
    return sum;
  }
};
