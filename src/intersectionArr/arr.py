class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {Solution().intersection(nums1, nums2)}")
