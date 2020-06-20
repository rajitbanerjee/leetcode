class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        # increment count of every char in s
        for char in s:
            if char not in seen:
                seen[char] = 0
            seen[char] += 1

        # decrement count of every char in t
        for char in t:
            if char not in seen:
                seen[char] = 0
            seen[char] -= 1

        # for anagrams, chars in s and t should have the same count
        for k, v in seen.items():
            if v != 0:
                return False

        return True


if __name__ == '__main__':
    s, t = '"anagram"', '"nagaram"'
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {Solution().isAnagram(s, t)}")
