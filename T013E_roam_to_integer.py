class Solution:

    def romanToInt(self, s: str) -> int:
        res, idx = 0, 0

        while idx < len(s):
            c = s[idx]
            if c == 'M':
                res += 1000
            elif c == 'D':
                res += 500
            elif c == 'L':
                res += 50
            elif c == 'V':
                res += 5
            elif c == 'C':
                if idx + 1 < len(s):
                    if s[idx + 1] == 'M':
                        res += 900
                        idx += 1
                    elif s[idx + 1] == 'D':
                        res += 400
                        idx += 1
                    else:
                        res += 100
                else:
                    res += 100
            elif c == 'X':
                if idx + 1 < len(s):
                    if s[idx + 1] == 'C':
                        res += 90
                        idx += 1
                    elif s[idx + 1] == 'L':
                        res += 40
                        idx += 1
                    else:
                        res += 10
                else:
                    res += 10
            else:
                if idx + 1 < len(s):
                    if s[idx + 1] == 'X':
                        res += 9
                        idx += 1
                    elif s[idx + 1] == 'V':
                        res += 4
                        idx += 1
                    else:
                        res += 1
                else:
                    res += 1

            idx += 1

        return res
