class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> list:
        res = set()
        
        def dfs(num, i):
            # N digits reached, add num to result
            if len(num) == N:
                res.add(int(num))
                return
            if 0 <= i - K:
                dfs(f"{num}{i - K}", i - K)
            if i + K < 10:
                dfs(f"{num}{i + K}", i + K)
        
        for i in range(10):
            if i == 0 and N != 1:
                continue
            dfs(str(i), i)

        return list(res)


if __name__ == '__main__':
    N = 3
    K = 7
    print(f"Input: N = {N}, K = {K}")
    print(f"Output: {Solution().numsSameConsecDiff(N, K)}")
