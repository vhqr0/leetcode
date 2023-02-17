class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len, top_len = 0, 0
        # stack: each unclosed open pair's level len
        # top_len: top level len, reset by unmatched close pair

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if stack:
                    cur_len = stack.pop() + 2
                    if stack:
                        stack[-1] += cur_len
                    else:
                        top_len += cur_len
                else:  # reset
                    max_len = max(max_len, top_len)
                    top_len = 0

        max_len = max(max_len, top_len)
        if stack:
            max_len = max(max_len, max(stack))

        return max_len

    def longestValidParentheses_dp(self, s: str) -> int:
        ls = len(s)
        cache = [[False for _ in range(ls + 1)] for _ in range(ls + 1)]

        # cache[i][j]:
        #   is s[i:j] valid?

        for i in range(ls + 1):
            # empty string is valid
            cache[i][i] = True

        max_len = 0

        for i in range(ls, -1, -1):
            p = i
            # skip s[i:i+1] for it's always False
            for j in range(i + 2, ls + 1):
                if s[j - 1] == '(':
                    cache[i][j] = False
                else:
                    # s[i:p] is max valid prefix, require s[p:j] is valid:
                    #   : s[p+1:j-1] is valid
                    #   : s[p], s[j-1] is pair
                    cache[i][j] = cache[p + 1][j - 1] and s[p] == '('
                    if cache[i][j]:
                        p = j
                        cur_len = j - i
                        if cur_len > max_len:
                            max_len = cur_len

        return max_len
