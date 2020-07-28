class Solution:
    def singleNumber(self, nums: list) -> int:
        res = nums[0]
        # XOR of all nums returns the lonely integer
        for n in nums[1:]:
            res ^= n
        return res


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(f"Input: nums = {nums}")
    print(f"Outut: {Solution().singleNumber(nums)}")
