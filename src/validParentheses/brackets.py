class Solution:
    def isValid(self, s: str) -> bool:
        def same(ch1: str, ch2: str) -> bool:
            table = {'(': ')', '{': '}', '[': ']'}
            return table[ch1] == ch2

        stk = []
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            elif ch in ")}]":
                if not (stk and same(stk.pop(), ch)):
                    return False
        return not stk


if __name__ == '__main__':
    s = input("Input: ")
    print(f"Output: {Solution().isValid(s)}")
