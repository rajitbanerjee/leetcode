class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(f"Input: {nums}")
    print(f"Output: {Solution().containsDuplicate(nums)}")
