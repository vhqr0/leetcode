from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_candidates(board: List[List[str]], i: int,
                           j: int) -> List[str]:
            g = set()
            for c in board[i]:
                g.add(c)
            for row in board:
                g.add(row[j])
            x, y = 3 * (i // 3), 3 * (j // 3)
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
            for i, j in idxes:
                g.add(board[i][j])
            candidates = list('123456789')
            return [c for c in candidates if c not in g]

        def solve(board: List[List[str]]) -> bool:

            # if solve failed, we should reset all modified cells
            modified_idxes = []

            candidate_maps = dict()

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        candidates = get_candidates(board, i, j)
                        if not candidates:
                            for idx in modified_idxes:
                                board[idx[0]][idx[1]] = '.'
                            return False
                        if len(candidates) == 1:
                            modified_idxes.append((i, j))
                            board[i][j] = candidates[0]
                        else:
                            candidate_maps[(i, j)] = candidates

            while True:
                modified = False
                removed_idxes = []  # del them after iteration
                for idx, candidates in candidate_maps.items():
                    new_candidates = get_candidates(board, idx[0], idx[1])
                    if len(new_candidates) < len(candidates):
                        modified = True
                        if len(new_candidates) == 1:
                            modified_idxes.append(idx)
                            board[idx[0]][idx[1]] = new_candidates[0]
                            removed_idxes.append(idx)
                        else:
                            candidate_maps[idx] = new_candidates
                for idx in removed_idxes:
                    del candidate_maps[idx]
                if not modified:
                    break

            if not candidate_maps:
                return True

            idx = min(candidate_maps, key=lambda idx: len(candidate_maps[idx]))
            modified_idxes.append(idx)

            for c in candidate_maps[idx]:
                board[idx[0]][idx[1]] = c
                if solve(board):
                    return True

            for idx in modified_idxes:
                board[idx[0]][idx[1]] = '.'
            return False

        if not solve(board):
            raise ValueError('solve failed')
