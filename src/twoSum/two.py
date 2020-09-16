from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                # complement number is already cached
                return [seen[target - n], i]
            # cache number and index
            seen[n] = i
        return [-1, -1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {Solution().twoSum(nums, target)}")
