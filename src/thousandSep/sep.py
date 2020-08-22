class Solution:
    def thousandSeparator(self, n: int) -> str:
        digits = list(str(n))
        for i in range(len(digits) - 3, 0, -3):
            digits.insert(i, '.')
        return ''.join(digits)


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().thousandSeparator(n)}")
