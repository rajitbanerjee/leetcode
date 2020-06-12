class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 1
        for i in range(1, n + 2):
            if i not in nums:
                return i


if __name__ == '__main__':
    nums = list(map(int, input("Input: ").split()))
    print(f"Output: {Solution().firstMissingPositive(nums)}")
