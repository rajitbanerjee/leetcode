# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self):
        ans = []
        while self:
            ans.append(self.val)
            self = self.next
        return ans


class Solution:
    def reorderList(self, head: ListNode) -> None:
        nums = []  # O(n) memory usage but simpler code
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next

        temp = head
        i, j = 0, len(nums) - 1
        while i <= j and temp:
            temp.val = nums[i]
            temp = temp.next
            if i != j:
                temp.val = nums[j]
                temp = temp.next
            i += 1
            j -= 1

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(f"Input: {head.toList()}")
    Solution().reorderList(head)
    print(f"Output: {head.toList()}")
