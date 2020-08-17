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
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        store = []
        while temp:
            store.append(temp.val)
            temp = temp.next
        return store == store[::-1]


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(f"Input: {head.toList()}")
    print(f"Output: {Solution().isPalindrome(head)}")
