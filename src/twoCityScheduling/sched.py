class Solution:
    def twoCitySchedCost(self, costs: list) -> int:
        # sort costs by the flying cost to city A - B
        costs.sort(key=lambda x: x[0] - x[1])
        # items in the first half of the list now store those flights
        #   which are cheaper to city A compared to the second half
        n = len(costs)
        A = [costs[i][0] for i in range(n//2)]
        B = [costs[i][1] for i in range(n//2, n)]
        return sum(A) + sum(B)


def main():
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    print(costs)
    print(Solution().twoCitySchedCost(costs))


main()
