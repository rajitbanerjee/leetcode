class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        p2, p3, p5 = 0, 0, 0
        for _ in range(n - 1):
            ans.append(min(ans[p2] * 2, ans[p3] * 3, ans[p5] * 5))
            if ans[-1] == ans[p2] * 2:
                p2 += 1
            if ans[-1] == ans[p3] * 3:
                p3 += 1
            if ans[-1] == ans[p5] * 5:
                p5 += 1
        return ans[-1]


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().nthUglyNumber(n)}")
