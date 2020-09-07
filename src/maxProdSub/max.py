from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currMin = currMax = globMax = nums[0]
        for n in nums[1:]:
            tempMin = min(n * currMin, n, n * currMax)
            tempMax = max(n * currMin, n, n * currMax)
            currMin, currMax = tempMin, tempMax
            globMax = max(currMax, globMax)

        return globMax


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(f"Input: nums = {nums}")
    print(f"Output: {Solution().maxProduct(nums)}")
