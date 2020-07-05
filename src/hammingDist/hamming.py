class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # bitwise XOR gives 1 for differing corresponding bits
        # sum of all the 1's gives the hamming distance
        return sum(map(int, list(bin(x ^ y))[2:]))


if __name__ == '__main__':
    x, y = 1, 4
    print(f"Input: x = {x}, y = {y}")
    print(f"Output: {Solution().hammingDistance(x, y)}")
