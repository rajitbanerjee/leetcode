class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # store results of subproblems
        dp = [1 for _ in range(n)]
        for _ in range(m - 1):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]


if __name__ == '__main__':
    m, n = 7, 3
    print(f"Input: m = {m}, n = {n}")
    print(f"Output: {Solution().uniquePaths(m, n)}")
