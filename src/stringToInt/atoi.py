class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        digits = ''
        for i, c in enumerate(s):
            if (i == 0 and self.isValidChar(c)) or c.isdigit():
                digits += c
            else:
                break

        try:
            num = int(digits)
            int_range = [-2**31, 2**31 - 1]
            if num < int_range[0]:
                return int_range[0]
            elif num > int_range[1]:
                return int_range[1]
            else:
                return num
        except:
            return 0

    def isValidChar(self, char: str) -> bool:
        return char.isdigit() or char in ['+', '-']


def main():
    print(f"Output: {Solution().myAtoi(input('Input: '))}")


main()
