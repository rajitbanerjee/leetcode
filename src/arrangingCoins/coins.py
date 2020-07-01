class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        while n >= count:
            n -= count
            count += 1
        return count - 1


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().arrangeCoins(n)}")
