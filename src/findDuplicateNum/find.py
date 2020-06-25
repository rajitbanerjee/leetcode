class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two pointers
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(f"Input: {nums}")
    print(f"Output: {Solution().findDuplicate(nums)}")
