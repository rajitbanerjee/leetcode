import random


class Solution:
    def __init__(self, w: list):
        self.cw = []  # cumulative weights
        self.total = 0
        for each in w:
            self.total += each
            self.cw.append(self.total)

    def pickIndex(self) -> int:
        # pick a random number from 1...total weight, then find the index it belongs to
        return self.search(random.randint(1, self.total), 0, len(self.cw) - 1)

    # binary search for index of random number in range of total weight
    def search(self, x: int, lo: int, hi: int) -> int:
        if lo <= hi:
            mid = lo + (hi - lo) // 2
            if x > self.cw[mid]:
                return self.search(x, mid + 1, hi)
            elif x < self.cw[mid]:
                return self.search(x, lo, mid - 1)
            else:
                return mid
        else:
            return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
