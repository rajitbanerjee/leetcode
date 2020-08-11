class Solution:
    def hIndex(self, citations: list) -> int:
        arr = sorted(citations, reverse=True)
        for i, c in enumerate(arr):
            if i >= c:
                return i
        return len(arr)


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(f"Input: {citations}")
    print(f"Output: {Solution().hIndex(citations)}")
