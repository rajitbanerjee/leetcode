class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, count = 0, 0
        for char in t:
            # subsequence has been found
            if count == len(s):
                return True
            # increase count of matching characters
            elif s[i] == char:
                i, count = i + 1, count + 1

        return count == len(s)


def main() -> None:
    s, t = input("Input:\ns = "), input("t = ")
    print(f"Output: {Solution().isSubsequence(s, t)}")


main()
