class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        res = []
        for i, w in enumerate(words):
            if w[0].lower() not in "aeiou":
                w = w[1:] + w[0]
            w += "ma" + ("a" * (i + 1))
            res.append(w)

        return ' '.join(res)


if __name__ == '__main__':
    S = input("Input: ")
    print(f"Output: {Solution().toGoatLatin(S)}")
