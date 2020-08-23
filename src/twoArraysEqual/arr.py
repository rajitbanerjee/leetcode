class Solution:
    def canBeEqual(self, target: list, arr: list) -> bool:
        return sorted(target) == sorted(arr)


if __name__ == '__main__':
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(f"Input: target = {target}, arr = {arr}")
    print(f"Output: {Solution().canBeEqual(target, arr)}")
