class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num // 2)


if __name__ == '__main__':
    num = int(input("Input: "))
    print(f"Output: {Solution().numberOfSteps(num)}")
