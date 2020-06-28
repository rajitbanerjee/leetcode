class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0

        def good(i: str) -> bool:
            if "3" in i or "4" in i or "7" in i:
                return False
            else:
                return "2" in i or "5" in i or \
                    "6" in i or "9" in i

        for i in range(1, N + 1):
            if good(str(i)):
                count += 1

        return count


if __name__ == '__main__':
    N = int(input("Input: "))
    print(f"Output: {Solution().rotatedDigits(N)}")
