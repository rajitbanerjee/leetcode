from collections import Counter


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        return [i for (i, _) in Counter(nums).most_common(k)]


if __name__ == '__main__':
    nums, k = [1, 1, 1, 2, 2, 3], 2
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {Solution().topKFrequent(nums, k)}")
