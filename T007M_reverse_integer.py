max_int = (1 << 31) - 1
min_int = -(1 << 31)

max_d, max_m = divmod(max_int, 10)
min_d, min_m = divmod(min_int, 10)

if min_m > 0:  # fix: [0, 9] => [-9, 0]
    min_d += 1
    min_m -= 10


class Solution:

    def reverse(self, x: int) -> int:
        res = 0

        if x < 0:
            while x != 0:
                x, m = divmod(x, 10)
                if m > 0:  # fix: [0, 9] => [-9, 0]
                    x += 1
                    m -= 10
                if res < min_d or (res == min_d and m < min_m):
                    return 0
                res = res * 10 + m
        else:
            while x != 0:
                x, m = divmod(x, 10)
                if res > max_d or (res == max_d and m > max_m):
                    return 0
                res = res * 10 + m

        return res
