class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            profit = max(profit, sell - buy)
            if sell < buy:
                buy = sell
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices}")
    print(f"Output: {Solution().maxProfit(prices)}")
