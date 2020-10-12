from itertools import product as cartesian
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return [''.join(i) for i in cartesian(*[phone[d] for d in digits])]


if __name__ == '__main__':
    digits = "23"
    print(f"Input: digits = {digits}")
    print(f"Output: {Solution().letterCombinations(digits)}")
