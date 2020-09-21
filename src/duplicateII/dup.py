from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False


if __name__ == '__main__':
    nums, k = [1, 2, 3, 1], 3
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {Solution().containsNearbyDuplicate(nums, k)}")
