from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i, n in enumerate(nums):
            total += n
            nums[i] = total
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(f"Input: {nums}")
    print(f"Output: {Solution().runningSum(nums)}")
