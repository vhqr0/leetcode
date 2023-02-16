class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = dict()
        beg, max_len = 0, 0
        for end in range(len(s)):
            c = s[end]
            if c in cache:
                beg = max(beg, cache[c] + 1)
            cache[c] = end
            max_len = max(max_len, end - beg + 1)
        return max_len
