class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # store results of subproblems
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if 0 in [i, j]:
                    dp[i][j] = 1
                else:
                    # any given grid index can be reached either from the top or left
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m-1][n-1]


if __name__ == '__main__':
    m, n = 7, 3
    print(f"Input: m = {m}, n = {n}")
    print(f"Output: {Solution().uniquePaths(m, n)}")
