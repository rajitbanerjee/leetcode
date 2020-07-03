class Solution:
    def prisonAfterNDays(self, cells: list, N: int) -> list:
        seen = set()
        cycle, size = False, 0
        # cells[0] and cells[-1] will always be 0
        # hence, there are 2^6 unique row arrangements
        # the idea is to find the cycle size in arrangements
        # then get the cell arrangement after (N % size) days
        for _ in range(N):
            new = self.nextDay(cells)
            if str(new) in seen:
                cycle = True
                break
            else:
                cells = new
                seen.add(str(cells))
                size += 1
        if cycle:
            return self.prisonAfterNDays(cells, N % size)
        else:
            return cells

    # find the cell arrangement on the next day
    def nextDay(self, cells: list) -> list:
        ans = [0]
        for i in range(1, len(cells) - 1):
            ans.append(int(cells[i-1] == cells[i+1]))
        ans.append(0)
        return ans


if __name__ == '__main__':
    cells, N = [0, 1, 0, 1, 1, 0, 0, 1],  7
    print(f"Input: cells = {cells}, N = {N}")
    print(f"Output: {Solution().prisonAfterNDays(cells, N)}")
