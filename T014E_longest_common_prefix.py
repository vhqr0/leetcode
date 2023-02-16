from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        bs = sorted(s.encode() for s in strs)
        b1, b2 = bs[0], bs[-1]
        min_len = min(len(b) for b in bs)

        for i in range(min_len):
            if b1[i] != b2[i]:
                return b1[:i].decode()
        else:
            return b1.decode()
