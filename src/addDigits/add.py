class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9  # cool pattern!


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().addDigits(n)}")
