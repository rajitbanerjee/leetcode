class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    num = int(input("Input: "))
    print(f"Output: {Solution().isPerfectSquare(num)}")
