class Solution:
    def sortColors(self, nums: list) -> None:
        lo, curr, hi = 0, 0, len(nums) - 1

        while curr <= hi:
            if nums[curr] == 0:
                # place 0's at the beginning
                nums[lo], nums[curr] = nums[curr], nums[lo]
                curr += 1
                lo += 1
            elif nums[curr] == 2:
                # place 2's at the end
                nums[curr], nums[hi] = nums[hi], nums[curr]
                hi -= 1
            else:
                curr += 1


if __name__ == '__main__':
    nums = [0, 2, 2, 1, 0, 2, 1, 1, 0]
    print(f"Input: {nums}")
    Solution().sortColors(nums)
    print(f"Output: {nums}")
