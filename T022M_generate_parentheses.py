from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']

        ps = set('(' + p + ')' for p in self.generateParenthesis(n - 1))

        for i in range(1, n // 2 + 1):
            j = n - i
            ps1 = self.generateParenthesis(i)
            ps2 = self.generateParenthesis(j)
            for p1 in ps1:
                for p2 in ps2:
                    ps.add(p1 + p2)
                    ps.add(p2 + p1)

        return list(ps)
