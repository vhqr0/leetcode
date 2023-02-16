class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        lh, ln = len(haystack), len(needle)

        offsets_map = [1 for _ in range(ln)]
        for idx in range(ln):
            has_matched = needle[:idx]
            o = 1
            while True:
                if len(has_matched) <= o:
                    break
                leading_matched = has_matched[o:]
                if needle.startswith(leading_matched):
                    break
                o += 1
            offsets_map[idx] = o

        pos, end = 0, lh - ln
        while pos <= end:
            for idx in range(ln):
                if haystack[pos + idx] != needle[idx]:
                    pos += offsets_map[idx]
                    break
            else:
                return pos

        return -1
