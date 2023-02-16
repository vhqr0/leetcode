max_int = (1 << 31) - 1
min_int = -(1 << 31)

max_d, max_m = divmod(max_int, 10)
min_d, min_m = divmod(min_int, 10)

if min_m > 0:  # fix: [0, 9] => [-9, 0]
    min_d += 1
    min_m -= 10


class Solution:

    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')

        if not s:
            return 0

        sign = s[0]
        neg = sign == '-'
        if sign in ('+', '-'):
            s = s[1:]

        res = 0

        for c in s:
            c = ord(c) - 48
            if not 0 <= c <= 9:
                break
            if neg:
                c = -c
                if res < min_d or (res == min_d and c < min_m):
                    return min_int
            else:
                if res > max_d or (res == max_d and c > max_m):
                    return max_int
            res = res * 10 + c

        return res
