class Solution:
    def titleToNumber(self, s: str) -> int:
        title_inv = s[::-1]
        col = 0
        # Essentially, base 26 to decimal
        for i, ch in enumerate(title_inpv):
            col += pow(26, i) * (ord(ch) - 64)
        return col


if __name__ == '__main__':
    s = input('Input: ')
    print(f"Output: {Solution().titleToNumber(s)}")
