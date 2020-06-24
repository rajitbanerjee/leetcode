class Solution:
    def __init__(self):
        self.trees = {}

    def numTrees(self, n: int) -> int:
        if n in [0, 1]:
            return 1

        if n in self.trees:
            return self.trees[n]

        self.trees[n] = 0
        # numTrees(n) = sigma 1, n { numtrees(i - i) * numTrees(n - i) }
        for i in range(1, n + 1):
            self.trees[n] += self.numTrees(i - 1) * self.numTrees(n - i)

        return self.trees[n]


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().numTrees(n)}")
