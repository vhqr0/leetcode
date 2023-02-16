from typing import Tuple

max_int = (1 << 31) - 1
min_int = -(1 << 31)


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        sign1 = dividend < 0
        sign2 = divisor < 0
        sign = not sign1 == sign2

        if sign1:
            dividend = -dividend
        if sign2:
            divisor = -divisor

        def _divmod(dividend: int, divisor: int) -> Tuple[int, int]:
            d, m = 0, dividend
            if dividend > divisor:
                d, m = _divmod(dividend, divisor << 1)
                d <<= 1
            while m >= divisor:
                d += 1
                m -= divisor
            return d, m

        d, _ = _divmod(dividend, divisor)

        if sign:
            d = -d
            d = max(d, min_int)
        else:
            d = min(d, max_int)

        return d
