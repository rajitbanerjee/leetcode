class Solution:
    def peakIndexInMountainArray(self, A: list) -> int:
        left, right = 1, len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                # peak found
                return mid
            elif A[mid] < A[mid + 1]:
                # still increasing left -> right
                left = mid + 1
            else:
                # decreasing left -> right
                right = mid - 1
        return -1


if __name__ == '__main__':
    A = [0, 2, 1, 0]
    print(f"Input: A = {A}")
    print(f"Output: {Solution().peakIndexInMountainArray(A)}")
