from math import factorial as f


class Solution:
    def getRow(self, rowIndex: int) -> list:
        res = []
        for i in range(rowIndex + 1):
            res.append(f(rowIndex)//(f(rowIndex - i) * f(i)))
        return res


if __name__ == '__main__':
    rowIndex = int(input("Input: "))
    print(f"Output: {Solution().getRow(rowIndex)}")
