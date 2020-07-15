class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == '__main__':
    s = input("Input: ")
    print(f"Output: {Solution().reverseWords(s)}")
