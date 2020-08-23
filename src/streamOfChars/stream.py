from collections import defaultdict


class StreamChecker:

    def __init__(self, words: list):
        self.s = ''
        self.words = defaultdict(set)
        for each in words:
            # store all words that end in a given letter
            self.words[each[-1]].add(each)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.words[letter])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
