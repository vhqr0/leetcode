#include <string>

using namespace std;

class Solution {
public:
  string intToRoman(int num) {
    string r;
    for (int i = num / 1000; i > 0; i--)
      r += "M";
    num %= 1000;
    if (num >= 900) {
      r += "CM";
      num -= 900;
    }
    if (num >= 500) {
      r += "D";
      num -= 500;
    }
    if (num >= 400) {
      r += "CD";
      num -= 400;
    }
    for (int i = num / 100; i > 0; i--)
      r += "C";
    num %= 100;
    if (num >= 90) {
      r += "XC";
      num -= 90;
    }
    if (num >= 50) {
      r += "L";
      num -= 50;
    }
    if (num >= 40) {
      r += "XL";
      num -= 40;
    }
    for (int i = num / 10; i > 0; i--)
      r += "X";
    num %= 10;
    if (num >= 9) {
      r += "IX";
      num -= 9;
    }
    if (num >= 5) {
      r += "V";
      num -= 5;
    }
    if (num >= 4) {
      r += "IV";
      num -= 4;
    }
    for (int i = 0; i < num; i++)
      r += "I";
    return r;
  }
};
