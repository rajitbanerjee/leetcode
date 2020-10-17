from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        freq = defaultdict(int)
        for i in range(len(s) - 9):
            freq[s[i: i + 10]] += 1
        return [k for k, v in freq.items() if v > 1]


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(f"Input: {s}")
    print(f"Output: {Solution().findRepeatedDnaSequences(s)}")
