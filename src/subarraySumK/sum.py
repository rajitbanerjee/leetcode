class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        freq = {0: 1}
        total, count = 0, 0
        
        for n in nums:
            total += n
            if total - k in freq:
                count += freq[total - k]
            freq[total] = freq.get(total, 0) + 1

        return count

if __name__ == '__main__':
    nums, k = [1, 2, 3], 3
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {Solution().subarraySum(nums, k)}")
        
        