class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2^x in binary is a 1 followed by 0s
        # 2^x - 1 in binary is a 0 followed by 1s
        # So the bitwise product must be 00...0
        return n and (n & (n - 1) == 0)


def main():
    n = int(input("Input: "))
    print(f"Output: {Solution().isPowerOfTwo(n)}")


main()
