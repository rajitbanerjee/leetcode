from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        for c in r_count:
            if c not in m_count or r_count[c] > m_count[c]:
                return False
        return True


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    print(f"Input: ransomNote = {ransomNote}, magazine = {magazine}")
    print(f"Output: {Solution().canConstruct(ransomNote, magazine)}")
