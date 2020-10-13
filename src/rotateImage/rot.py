from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                # transpose
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse transposed rows
        for i, row in enumerate(matrix):
            matrix[i][:] = row[::-1]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Input: {matrix}")
    Solution().rotate(matrix)
    print(f"Output: {matrix}")
