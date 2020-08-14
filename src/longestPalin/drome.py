from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        for v in Counter(s).values():
            # add all pairs of characters to palindrome length
            longest += (v // 2) * 2
            # this is only executed once (when an odd value is found)
            if (longest % 2 == 0) and (v & 1):
                longest += 1
        return longest


if __name__ == '__main__':
    s = input("Input: ")
    print(f"Output: {Solution().longestPalindrome(s)}")
