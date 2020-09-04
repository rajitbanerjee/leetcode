class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n)]

        def count(i: int, n: int):
            if i > n:
                return 0
            if i == n:
                return 1
            if not memo[i]:
                memo[i] = count(i + 1, n) + count(i + 2, n)
            return memo[i]

        return count(0, n)


if __name__ == '__main__':
    n = int(input("Input: n = "))
    print(f"Output: {Solution().climbStairs(n)}")
