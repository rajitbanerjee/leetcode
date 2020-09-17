class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        d = 0

        while True:
            for s in instructions:
                if s == 'G':
                    if d in [0, 2]:
                        pos[1] += 1 if d == 0 else -1
                    else:
                        pos[0] += 1 if d == 1 else -1
                else:
                    d = (d + (1 if s == 'L' else -1)) % 4

            if d == 0:
                return pos == [0, 0]


if __name__ == '__main__':
    ins = input("Input: ")
    print(f"Output: {Solution().isRobotBounded(ins)}")
