from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend([nums[i], nums[i+n]])
        return res


if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(f"Input: nums = {nums}, n = {n}")
    print(f"Output: {Solution().shuffle(nums, n)}")
