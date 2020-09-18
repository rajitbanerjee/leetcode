from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sub = ""
        min_s = min(strs, key=len)
        for i in range(len(min_s)):
            sub += min_s[i]
            if not all(s.startswith(sub) for s in strs):
                return sub[:-1]
        return sub


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(f"Input: {strs}")
    print(f"Output: {Solution().longestCommonPrefix(strs)}")
