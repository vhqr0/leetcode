class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if (p, c) not in (('(', ')'), ('[', ']'), ('{', '}')):
                    return False
        return len(stack) == 0
