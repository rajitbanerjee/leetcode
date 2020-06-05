class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


def main():
    arr = list('hello')
    print(f"Input:\t{arr}")
    Solution().reverseString(arr)
    print(f"Output:\t{arr}")


main()
