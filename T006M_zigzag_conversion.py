class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        ss = list('' for _ in range(numRows))

        block_size = (numRows - 1) * 2

        for i in range(len(s)):
            j = i % block_size
            if j < numRows:
                ss[j] += s[i]
            else:
                ss[block_size - j] += s[i]

        return ''.join(ss)
