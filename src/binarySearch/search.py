class Solution:
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    nums, target = [-1, 0, 3, 5, 9, 12], 9
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {Solution().search(nums, target)}")
