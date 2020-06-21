class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            ans = ""
            compact = self.getCompact(prev)
            for dig in compact:
                (prev, count) = self.getCount(dig, prev)
                ans += str(count) + dig
            return ans

    # remove consecutive duplicates
    def getCompact(self, prev: str) -> str:
        ans = ['']
        for dig in prev:
            if ans[-1] != dig:
                ans.append(dig)
        return ''.join(ans)

    # count number of digits in groups of given digit
    def getCount(self, dig: str, prev: str) -> (str, int):
        count = 0
        while (len(prev) > 0 and prev[0] == dig):
            prev = prev[1:]
            count += 1
        return (prev, count)


print(Solution().countAndSay(int(input("Input: "))))
