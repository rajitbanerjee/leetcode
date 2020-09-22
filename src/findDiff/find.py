class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for ch in s:
            if ch not in seen:
                seen[ch] = 0
            seen[ch] += 1

        for ch in t:
            if ch in seen and seen[ch] > 0:
                seen[ch] -= 1
            else:
                return ch

        return ""


if __name__ == '__main__':
    s = "abcd"
    t = "bdeac"
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {Solution().findTheDifference(s, t)}")
