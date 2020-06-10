class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return lo


def main() -> None:
    nums = [1, 3, 5, 6]
    target = 5
    print(f"Input: {nums}, {target}")
    print(f"Output: {Solution().searchInsert(nums, target)}")


main()
