class NumArray:

    def __init__(self, nums: List[int]):
        self.running = [0]
        for n in nums:
            # cumulative sum
            self.running.append(self.running[-1] + n)
        print(self.running)

    def sumRange(self, i: int, j: int) -> int:
        return self.running[j + 1] - self.running[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
