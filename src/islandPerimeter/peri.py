class Solution:
    def islandPerimeter(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])

        # check if grid[i][j] is out of bounds or 0
        def isWater(i: int, j: int) -> int:
            return int(i < 0 or i >= m or j < 0 or
                       j >= n or grid[i][j] == 0)

        def countPeri(i: int, j: int) -> int:
            return isWater(i - 1, j) + isWater(i + 1, j) + \
                isWater(i, j - 1) + isWater(i, j + 1)

        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += countPeri(i, j)

        return perimeter
