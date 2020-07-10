class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        count = 0
        for s in S:
            count += int(s in jewels)
        return count


if __name__ == '__main__':
    j, s = "aA", "aAAbbbb"
    print(f"Input: J = {j}, S = {s}")
    print(f"Output: {Solution().numJewelsInStones(j, s)}")
