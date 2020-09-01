from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def isValid(time: str) -> bool:
            return 0 <= int(time[:2]) <= 23 and 0 <= int(time[3:]) <= 59

        times = sorted(
            [f"{p[0]}{p[1]}:{p[2]}{p[3]}" for p in permutations(A)], reverse=True)
        for t in times:
            if isValid(t):
                return t
        return ""


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print(f"Input: A = {A}")
    print(f"Output: {Solution().largestTimeFromDigits(A)}")
