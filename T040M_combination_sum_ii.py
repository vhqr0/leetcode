from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def get_combs(beg: int, path: List[int], target: int):
            if target == 0:
                res.append(path)
                return

            for i in range(beg, len(candidates)):
                c = candidates[i]
                if i > beg and c == candidates[i - 1]:
                    continue
                if c > target:
                    break
                get_combs(i + 1, path + [c], target - c)

        get_combs(0, [], target)
        return res
