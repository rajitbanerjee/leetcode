from math import log

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return int(log(num)/log(4)) == log(num)/log(4)

if __name__ == '__main__':
    num = int(input('Input: '))
    print(f"Output: {Solution().isPowerOfFour(num)}")

