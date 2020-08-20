class Solution:
    def generateParenthesis(self, n: int) -> list:

        def backtrack(res: list, s: str, left: int, right: int) -> None:
            # no more closing brackets available, cannot open any new ones
            if not right:
                res.append(s)
                return
            # still have opening brackets available
            if left > 0:
                backtrack(res, s + '(', left - 1, right)
            # still have more brackets available to close exiting open ones
            if right > left:
                backtrack(res, s + ')', left, right - 1)

        res = []
        # both opening and closing brackets are limited to n each
        backtrack(res, "", n, n)
        return res


if __name__ == '__main__':
    n = int(input("Input: "))
    print(f"Output: {Solution().generateParenthesis(n)}")
