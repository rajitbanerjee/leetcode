from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def findCost(i: int):
            if i == len(cost):
                # target reached
                return 0
            elif i > len(cost):
                # out of range for cost values
                return 1000

            if not memo[i]:
                memo[i] = cost[i] + min(findCost(i+1), findCost(i+2))
            return memo[i]

        memo = [0 for _ in range(len(cost) + 2)]
        return min(findCost(0), findCost(1))


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f"Input: cost = {cost}")
    print(f"Output: {Solution().minCostClimbingStairs(cost)}")
