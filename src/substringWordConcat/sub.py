class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if s == "" or len(words) == 0:
            return []
        else:
            indices = []
            n = len(words[0])
            size = len(words) * n
            for i in range(len(s) - size + 1):
                if self.containsAll(s[i: i + size], words, size, n):
                    indices.append(i)
            return indices

    def containsAll(self, sub: list, words: list, size: int, n: int) -> bool:
        sub_words = []
        for i in range(0, size, n):
            sub_words.append(sub[i: i + n])

        return sorted(sub_words) == sorted(words)
