from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums) * (len(nums) + 1) // 2
        return total - sum(nums)


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Input: {nums}")
    print(f"Output: {Solution().missingNumber(nums)}")
