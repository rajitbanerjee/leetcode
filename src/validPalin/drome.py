class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s.lower() if ch.isalnum())
        return s == s[::-1]


if __name__ == '__main__':
    s = input("Input: ")
    print(f"Output: {Solution().isPalindrome(s)}")
