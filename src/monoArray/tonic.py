from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i] <= A[i+1] for i in range(len(A)-1)) or \
            all(A[i] >= A[i+1] for i in range(len(A)-1))


if __name__ == '__main__':
    A = [1, 2, 2, 3]
    print(f"Input: {A}")
    print(f"Output: {Solution().isMonotonic(A)}")
