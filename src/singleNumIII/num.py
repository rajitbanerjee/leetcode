class Solution:
    def singleNumber(self, nums: list) -> list:
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)
        return list(seen)


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    print(f"Input: nums = {nums}")
    print(f"Output: {Solution().singleNumber(nums)}")
