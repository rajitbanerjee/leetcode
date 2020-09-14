import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        if left == right:
            return [-1, -1]
        else:
            return [left, right - 1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(f"Input: number = {nums}, target = {target}")
    print(f"Output: {Solution().searchRange(nums, target)}")
