class Solution:
    def tictactoe(self, moves: list) -> str:
        # fill board
        board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(len(moves)):
            board[moves[i][0]][moves[i][1]] = "X" if (i % 2 == 0) else "O"

        # separate diagonals, rows and columns
        diag, row, col = ["", ""], ["", "", ""], ["", "", ""]
        for i in range(3):
            for j in range(3):
                if i == j:
                    diag[0] += board[i][i]
                if i + j == 2:
                    diag[1] += board[i][j]
                row[i] += board[i][j]
                col[i] += board[j][i]

        def hasBlank(board: list) -> bool:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        return True
            return False

        # determine winner
        if "XXX" in row or "XXX" in col or "XXX" in diag:
            return "A"
        elif "OOO" in row or "OOO" in col or "OOO" in diag:
            return "B"
        elif hasBlank(board):
            return "Pending"
        else:
            return "Draw"


if __name__ == '__main__':
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print(f"Input: moves = {moves}")
    print(f"Output: {Solution().tictactoe(moves)}")
