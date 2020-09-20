# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getList(self):
        ans = []
        while self:
            ans.append(str(self.val))
            self = self.next
        return "->".join(ans)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(1, ListNode(2))))
    print(f"Input: {head.getList()}")
    Solution().deleteDuplicates(head)
    print(f"Output: {head.getList()}")
