class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = [ch for ch in s[::-1] if ch.lower() in "aeiou"]
        chars = list(s)
        x = 0
        for i, ch in enumerate(chars):
            if ch.lower() in "aeiou":
                chars[i] = vows[x]
                x += 1
        return "".join(chars)


if __name__ == '__main__':
    s = input("Input: ")
    print(f"Output: {Solution().reverseVowels(s)}")
