class Solution:
    def singleNumber(self, nums: list) -> int:
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1

        for k, v in seen.items():
            if v == 1:
                return k

        return 0


if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    print(f"Input: {nums}")
    print(f"Output: {Solution().singleNumber(nums)}")
