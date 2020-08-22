"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class CustomFunction:
    def f(self, x, y):
        return x + y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> list:
        res = []
        for x in range(1, z + 1):
            left, right = 1, z
            while left <= right:
                y = left + (right - left) // 2
                if customfunction.f(x, y) == z:
                    res.append([x, y])
                    break
                elif customfunction.f(x, y) > z:
                    right = y - 1
                else:
                    left = y + 1
        return res


if __name__ == '__main__':
    func, z = CustomFunction(), 5
    print(f"Input: function = f(x, y) = x + y, z = {z}")
    print(f"Output: {Solution().findSolution(func, z)}")
