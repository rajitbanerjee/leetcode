from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == target - n:
                    return [i + 1, mid + 1]
                elif numbers[mid] < target - n:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: numbers = {nums}, target = {target}")
    print(f"Output: {Solution().twoSum(nums, target)}")
