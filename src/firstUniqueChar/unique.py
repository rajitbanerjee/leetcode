import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = []
        for char in string.ascii_lowercase:
            if s.count(char) == 1:
                unique.append(s.index(char))
        if len(unique) == 0:
            return -1
        else:
            return min(unique)


if __name__ == "__main__":
    s = input("Input: ")
    print(f"Output: {Solution().firstUniqChar(s)}")
