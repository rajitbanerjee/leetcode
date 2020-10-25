from collections import Counter
from math import factorial as f
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def c(n: int, k: int) -> int:
            return f(n)//(f(k) * f(n - k))

        freq = Counter(nums)
        return sum(c(i, 2) for i in freq.values() if i >= 2)


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    print(f"Input: {nums}")
    print(f"Output: {Solution().numIdenticalPairs(nums)}")
