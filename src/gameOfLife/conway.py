from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        res = [[0 for _ in range(m)] for _ in range(n)]

        def getVal(i, j):
            if 0 <= i < n and 0 <= j < m:
                return board[i][j]
            else:
                return -1

        def countAlive(i, j):
            alive = 0
            idx = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                   (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            for ix in idx:
                if getVal(ix[0], ix[1]) == 1:
                    alive += 1
            return alive

        for i in range(n):
            for j in range(m):
                alive = countAlive(i, j)
                if board[i][j]:
                    if alive in [2, 3]:
                        res[i][j] = 1
                else:
                    if alive == 3:
                        res[i][j] = 1
        board[:] = res


if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print(f"Input: {board}")
    Solution().gameOfLife(board)
    print(f"Output: {board}")
