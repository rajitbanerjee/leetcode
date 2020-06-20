from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        for each in list(permutations(range(1, n + 1)))[k - 1]:
            ans += str(each)
        return ans


if __name__ == '__main__':
    n, k = 3, 3
    print(f"Input: n = {n}, k = {k}")
    print(f"Output: {Solution().getPermutation(n, k)}")
