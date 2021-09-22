#include <vector>

using namespace std;

#define SIZE (2 << 14)
#define HASH(x) ((x) & (SIZE - 1))

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    short ht[SIZE] = {0};
    for (int i = 0; i < nums.size(); i++) {
      int index = HASH(target - nums[i]);
      if (ht[index] != 0)
        return {ht[index] - 1, i};
      ht[HASH(nums[i])] = i + 1;
    }
    return {};
  }
};
