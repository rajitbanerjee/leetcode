from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        return list(groups.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: strs = {strs}")
    print(f"Output: {Solution().groupAnagrams(strs)}")
