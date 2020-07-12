class Solution:
    def reverseBits(self, n: int) -> int:
        rev = ('{0:032b}'.format(n))[::-1]
        return int(rev, base=2)


if __name__ == '__main__':
    n = int(input("Input: "), base=2)
    print(f"Output: {'{0:032b}'.format(Solution().reverseBits(n))}")
