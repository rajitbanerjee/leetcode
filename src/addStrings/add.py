class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


if __name__ == '__main__':
    n1, n2 = 10, 20
    print(f"Input: n1 = {n1}, n2 = {n2}")
    print(f"Output: {Solution().addStrings(n1, n2)}")
