class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices}")
    print(f"Output: {Solution().maxProfit(prices)}")
