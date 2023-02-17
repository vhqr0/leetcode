from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid(g: List[str]) -> bool:
            for i in range(len(g)):
                for j in range(i + 1, len(g)):
                    if g[i] == g[j]:
                        return False
            return True

        for row in board:
            if not valid([c for c in row if c != '.']):
                return False

        for i in range(9):
            if not valid([row[i] for row in board if row[i] != '.']):
                return False

        for i in range(3):
            for j in range(3):
                x, y = 3 * i, 3 * j
                idxes = (
                    (x, y),
                    (x, y + 1),
                    (x, y + 2),
                    (x + 1, y),
                    (x + 1, y + 1),
                    (x + 1, y + 2),
                    (x + 2, y),
                    (x + 2, y + 1),
                    (x + 2, y + 2),
                )
                g = [board[i][j] for i, j in idxes if board[i][j] != '.']
                if not valid(g):
                    return False

        return True
