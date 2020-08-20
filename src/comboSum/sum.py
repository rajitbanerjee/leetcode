class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []

        def dfs(target, nums, curr):
            if target == 0:
                res.append(curr)
                return
            for i, n in enumerate(nums):
                if n > target:
                    # exit current path, n is too large for target
                    break
                # if n is used, target - n is left (needs to be searched for)
                left = target - n
                if left == 0 or nums[0] <= left:
                    # n is added to current path
                    dfs(left, nums[i:], curr + [n])

        dfs(target, sorted(candidates), [])
        return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Input: candidates = {candidates}, target = {target}")
    print(f"Output: {Solution().combinationSum(candidates, target)}")
