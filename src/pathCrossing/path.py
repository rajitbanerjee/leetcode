class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(x, y)}
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            else:
                x -= 1

            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False


if __name__ == '__main__':
    path = input("Input: ")
    print(f"Output: {Solution().isPathCrossing(path)}")
