from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {Solution().coinChange(coins, amount)}")
