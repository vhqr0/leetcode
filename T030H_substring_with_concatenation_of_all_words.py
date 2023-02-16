from collections import Counter

from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # uniq words, calc weights
        # [word, good, best, word] => [word, good, best], [2, 1, 1]
        counter = Counter(words)
        words = list(counter)
        weights = [counter[word] for word in words]
        # wn1: words num
        # wn2: uniq words num
        wn1, wn2, wl = sum(weights), len(words), len(words[0])

        cache = dict()
        for idx, word in enumerate(words):
            cache[word] = idx

        # idx of word at point
        word_maps = [-1 for _ in range(len(s))]
        for i in range(len(s) - wl + 1):
            word = s[i:i + wl]
            idx = cache.get(word)
            if idx is not None:
                word_maps[i] = idx

        res = []
        for i in range(wl):
            sub_maps = word_maps[i::wl]
            for j in range(len(sub_maps) - wn1 + 1):
                # check sub_maps[j:j+wn1]: compare weights
                for k in range(wn1):
                    if sub_maps[j + k] == -1:
                        break
                else:
                    cur_weights = [0 for _ in range(wn2)]
                    for k in range(wn1):
                        cur_weights[sub_maps[j + k]] += 1
                    for k in range(wn2):
                        if cur_weights[k] != weights[k]:
                            break
                    else:
                        res.append(i + wl * j)

        return res
