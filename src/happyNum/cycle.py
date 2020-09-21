class Solution:
    def isHappy(self, n: int) -> bool:
        def ssd(n):
            return sum(int(i) ** 2 for i in str(n))

        slow = ssd(n)
        fast = ssd(ssd(n))

        while slow != fast and fast != 1:
            slow = ssd(slow)
            fast = ssd(ssd(fast))

        return fast == 1


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().isHappy(n)}")
