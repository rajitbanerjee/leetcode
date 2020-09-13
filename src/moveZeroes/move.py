from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) - 1:
            # all zeroes have been moved
            if i == len(nums) - nums.count(0):
                break

            if nums[i] == 0:
                # find next non-zero element index
                j = i + 1
                while nums[j] == 0:
                    j += 1

                # swap
                nums[i], nums[j] = nums[j], nums[i]

            i += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(f"Input: {nums}")
    Solution().moveZeroes(nums)
    print(f"Output: {nums}")
