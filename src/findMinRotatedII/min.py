class Solution:
    def findMin(self, nums: list) -> int:
        n = len(nums)
        if not nums:
            return -1
        if n == 1:
            return nums[0]
        # initialise min index p = 0
        p = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                # reassign p to smaller nums index
                p = i
                break
        return nums[p]


if __name__ == '__main__':
    nums = [2, 2, 2, 0, 1, 2]
    print(f"Input: nums = {nums}")
    print(f"Output: {Solution().findMin(nums)}")
