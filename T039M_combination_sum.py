from typing import List, Set


class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:

        def get_combs(candidates: Set[int], target: int) -> List[List[int]]:
            res = []
            for c in list(candidates):
                if c == target:
                    res.append([c])
                elif c < target:
                    for comb in get_combs(candidates.copy(), target - c):
                        comb.append(c)
                        res.append(comb)
                candidates.remove(c)
            return res

        return get_combs(set(candidates), target)
