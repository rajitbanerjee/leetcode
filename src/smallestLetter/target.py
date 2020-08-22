class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        left, right = 0, len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[right]


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "a"
    print(f"Input: letters = {letters}, target = {target}")
    print(f"Output: {Solution().nextGreatestLetter(letters, target)}")
