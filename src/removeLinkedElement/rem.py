# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(next=head)
        prev, curr = temp, head

        while curr:
            if curr.val == val:
                # reassign pointers if value is found
                prev.next = curr.next
            else:
                # move on
                prev = curr
            curr = curr.next
        return temp.next


def printList(head: ListNode) -> list:
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return ('->'.join(res))


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    val = 1
    print(printList(head))
    print(f"Input: {printList(head)}, val = {val}")
    print(f"Output: {printList(Solution().removeElements(head, val))}")
