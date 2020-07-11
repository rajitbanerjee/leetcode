class Solution:
    def subsets(self, nums: list) -> list:
        if len(nums) == 0:
            return [[]]
        
        # assume that a smaller case works
        s = self.subsets(nums[1:])
        # attach nums[0] to every sublist in smaller answer
        for each in s[:]:
            new = [nums[0]]
            new.extend(each)
            s.append(new)
        return s