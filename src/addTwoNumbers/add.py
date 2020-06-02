# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        temp = ListNode()
        ans = temp
        carry = 0

        while l1 or l2 or carry:
            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            total = dig1 + dig2 + carry
            carry = total // 10

            temp.next = ListNode(total % 10)
            temp = temp.next

        return ans.next


def printList(start) -> list:
    temp = start
    ans = []
    while temp != None:
        ans.append(temp.val)
        temp = temp.next
    return ans


def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    print("Input:", str(printList(l1)), str(printList(l2)))
    total = Solution().addTwoNumbers(l1, l2)
    print("Output:", str(printList(total)))


main()
