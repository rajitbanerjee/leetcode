class Solution:
    def hIndex(self, citations: list) -> int:
        n = len(citations)
        lo, hi = 0, n - 1
        # Modified binary search
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if n - 1 - mid < citations[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return n - lo


if __name__ == '__main__':
    citations = [0, 1, 3, 5, 6]
    print(f"Input: {citations}")
    print(f"Output: {Solution().hIndex(citations)}")
