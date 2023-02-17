from typing import List


class Solution:

    def countAndSay(self, n: int) -> str:

        def say(n: int) -> List[int]:
            if n == 1:
                return [1]

            prev_say = say(n - 1)

            res = []

            for idx, num in enumerate(prev_say):
                if idx != 0 and prev_say[idx - 1] == prev_say[idx]:
                    res[-2] += 1
                else:
                    res.append(1)
                    res.append(num)

            return res

        res = say(n)

        return ''.join(str(r) for r in res)
