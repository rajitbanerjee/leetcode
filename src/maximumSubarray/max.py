class Solution:
    def maxSubArray(self, nums: list) -> int:
        curr = glob = nums[0]
        for n in nums[1:]:
            # either add n to current max, or start the current max from n
            curr = max(n + curr, n)
            # update the global max accordingly
            glob = max(glob, curr)
        return glob


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {nums}")
    print(f"Output: {Solution().maxSubArray(nums)}")
