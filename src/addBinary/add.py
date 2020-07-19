class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a, b = "1010", "1011"
    print(f"Input: a = {a}, b = {b}")
    print(f"Output: {Solution().addBinary(a, b)}")
