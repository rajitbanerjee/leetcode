class Solution:
    def change(self, amount: int, coins: list) -> int:
        # to store the number of solutions for each value index
        table = [0 for k in range(amount + 1)]
        # amount = 0 can be obtained by selecting no coins (1 way)
        table[0] = 1

        # pick all coins in order
        for i in range(0, len(coins)):
            # update table values
            for j in range(coins[i], amount + 1):
                table[j] += table[j - coins[i]]

        # number of solutions for required amount
        return table[amount]


def main() -> None:
    amount, coins = 5, [1, 2, 5]
    print(f"Input: amount = {amount}, coins = {coins}")
    print(f"Output: {Solution().change(amount, coins)}")


main()
