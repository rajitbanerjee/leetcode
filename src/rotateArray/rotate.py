class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # Remember nums[:] is needed to modify the list elements in-place
        nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Input: nums = {nums}, k = {k}")
    Solution().rotate(nums, k)
    print(f"Output: {nums}")
