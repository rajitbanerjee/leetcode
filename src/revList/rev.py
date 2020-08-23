# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self) -> list:
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return res

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3)))
    print(f"Input: {head.toList()}")
    head = Solution().reverseList(head)
    print(f"Output: {head.toList()}")
    
