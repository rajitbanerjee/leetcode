class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N % 2


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().divisorGame(n)}")
