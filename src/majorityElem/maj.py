from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(f"Input: {nums}")
    print(f"Ouput: {Solution().majorityElement(nums)}")
