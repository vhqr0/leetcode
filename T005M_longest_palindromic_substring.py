class Solution:

    def longestPalindrome(self, s: str) -> str:
        max_len, max_pos = 0, 0

        for i in range(len(s)):
            c = s[i]
            beg, end = i, i

            # baaaaaaaaaaab
            #  _beg
            #  _end

            for j in range(i + 1, len(s)):
                if s[j] != c:
                    break
                end += 1

            # baaaaaaaaaaab
            #  _beg
            #            _end

            while beg >= 1 and end < len(s) - 1 and s[beg - 1] == s[end + 1]:
                beg -= 1
                end += 1

            cur_len = end - beg + 1

            if cur_len > max_len:
                max_len = cur_len
                max_pos = beg

        return s[max_pos:max_pos + max_len]
