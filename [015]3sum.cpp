#include <algorithm>
#include <vector>

using namespace std;

#define SIZE (2 << 14)
#define HASH(x) ((x) & (SIZE - 1))

class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    vector<vector<int>> res;
    vector<pair<int, int>> ht[SIZE];
    for (int i = 0; i < nums.size(); i++) {
      vector<pair<int, int>> pairs = ht[HASH(-nums[i])];
      for (auto pair : pairs)
        res.push_back({pair.first, pair.second, nums[i]});
      pairs.clear();
      for (int j = 0; j < i; j++)
        ht[HASH(nums[i] + nums[j])].push_back({nums[i], nums[j]});
    }
    return res;
  }
};
