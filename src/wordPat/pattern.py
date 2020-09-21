class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        seen = {}

        for ch, w in zip(pattern, words):
            if ch in seen and seen[ch] != w:
                return False
            seen[ch] = w
        return len(set(words)) == len(set(pattern)) and len(words) == len(pattern)


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(f"Input: pattern = {pattern}, s = {s}")
    print(f"Output: {Solution().wordPattern(pattern, s)}")
