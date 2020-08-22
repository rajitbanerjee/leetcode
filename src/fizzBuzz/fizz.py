class Solution:
    def fizzBuzz(self, n: int) -> list:
        res = []
        maps = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n + 1):
            ans = ""
            for k, v in maps.items():
                if i % k == 0:
                    ans += v
            if not ans:
                ans = str(i)
            res.append(ans)
        return res


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().fizzBuzz(n)}")
