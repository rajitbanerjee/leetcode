from math import factorial as f


class Solution:
    def generate(self, numRows: int) -> list:

        def getRow(rowIndex: int) -> list:
            res = []
            for i in range(rowIndex + 1):
                res.append(f(rowIndex)//(f(rowIndex - i) * f(i)))
            return res

        return [getRow(i) for i in range(numRows)]


if __name__ == '__main__':
    numRows = int(input("Input: "))
    print(f"Output: {Solution().generate(numRows)}")
