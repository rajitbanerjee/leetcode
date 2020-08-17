from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list, H: int) -> int:
        def canEat(k) -> bool:
            return sum([ceil(p / k) for p in piles]) <= H

        # find minimum k such that condition canEat(k) is satisfied
        left, right = 1, max(piles)
        while left < right:
            k = left + (right - left) // 2
            if canEat(k):
                right = k
            else:
                left = k + 1
        return left


if __name__ == '__main__':
    piles, H = [3, 6, 7, 11], 8
    print(f"Input: piles = {piles}, H = {H}")
    print(f"Output: {Solution().minEatingSpeed(piles, H)}")
