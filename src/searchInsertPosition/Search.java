package searchInsertPosition;

public class Search {
    public int searchInsert(int[] nums, int target) {
        if (target < nums[0]) {
            return 0;
        } else if (target > nums[nums.length - 1]) {
            return nums.length;
        } else {
            return binarySearch(nums, target, 0, nums.length);
        }
    }

    // modify standard binary search to return lo when n not in a[]
    private static int binarySearch(int[] a, int n, int lo, int hi) {
        if (lo > hi) {
            return lo;
        }
        int mid = lo + (hi - lo) / 2;
        if (a[mid] > n) {
            return binarySearch(a, n, lo, mid - 1);
        } else if (a[mid] < n) {
            return binarySearch(a, n, mid + 1, hi);
        } else {
            return mid;
        }
    }
}
