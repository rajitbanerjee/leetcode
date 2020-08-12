class Solution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if not nums:
            return 0
        elif n < 2:
            return nums[0]
        else:
            dp = [0 for _ in range(n + 2)]
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])

            # either rob the current house, or the previous one
            for i in range(2, n):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

            return dp[n - 1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(f"Input: {nums}")
    print(f"Output: {Solution().rob(nums)}")
