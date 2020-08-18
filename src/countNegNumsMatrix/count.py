class Solution:
    def countNegatives(self, grid: list) -> int:
        def search(row) -> int:
            left, right = 0, len(row)
            while left < right:
                mid = left + (right - left) // 2
                # Condition: find the index where negative nums start
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            return len(row) - left

        count = 0
        for row in grid:
            count += search(row)
        return count


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(f"Input: grid = {grid}")
    print(f"Output: {Solution().countNegatives(grid)}")
