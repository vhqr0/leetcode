class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        cache = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]

        # cache[i][j]:
        #   is s[:i] match p[:j]?

        cache[0][0] = True
        for i in range(2, lp + 1):
            # if empty string match p[:i-2] and p[i-1] == '*'
            cache[0][i] = cache[0][i - 2] and p[i - 1] == '*'
        for i in range(1, ls + 1):
            # nonempty string doesn't match ''
            cache[i][0] = False
        for j in range(1, lp + 1):
            for i in range(1, ls + 1):
                if p[j - 1] == '*':
                    # case 1: s[:i] match p[:j-2]
                    #   escape tail [any]*
                    # case 2: s[:i-1] match p[:j]
                    #   expand tail [?]* where ? is '.' or s[i-1]
                    cache[i][j] = cache[i][j - 2] or \
                        (cache[i - 1][j] and
                         (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
                else:
                    # s[:i-1] match p[:j-1] and s[i-1] match p[j-1]
                    cache[i][j] = cache[i - 1][j - 1] and \
                        (p[j - 1] == '.' or p[j - 1] == s[i - 1])

        return cache[ls][lp]
