class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])

        # Mark * all O's on the border and the O's connected to them
        def dfs(board: list, i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = '*'
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)

        for i in range(m):
            for j in range(n):
                if i in [0, m - 1] or j in [0, n - 1]:
                    dfs(board, i, j)

        # Change O's to X's, then *'s back to O's
        def replace(board: list, old: str, new: str) -> None:
            for i, row in enumerate(board):
                board[i] = [item.replace(old, new) for item in row]

        replace(board, 'O', 'X')
        replace(board, '*', 'O')


def display(board: list) -> None:
    for row in board:
        print(" ".join(row))
    print()


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print("Input:")
    display(board)
    Solution().solve(board)
    print("Output:")
    display(board)
