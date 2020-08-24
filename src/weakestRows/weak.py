from collections import OrderedDict


class Solution:
    def kWeakestRows(self, mat: list, k: int) -> list:
        rows = {i: mat[i] for i in range(len(mat))}
        # life is short, use python
        rows = OrderedDict(sorted(rows.items(), key=lambda kv: sum(kv[1])))
        return list(rows.keys())[:k]


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1]]
    k = 3

    print(f"Input: mat = {mat}, k = {k}")
    print(f"Output: {Solution().kWeakestRows(mat, k)}")
