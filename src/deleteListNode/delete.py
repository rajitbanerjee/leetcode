# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def printList(start) -> list:
    temp = start
    ans = []
    while temp != None:
        ans.append(temp.val)
        temp = temp.next
    return ans


def main() -> None:
    head = ListNode(4)
    a = ListNode(5)
    b = ListNode(1)
    c = ListNode(9)

    head.next = a
    a.next = b
    b.next = c

    print("Input: " + str(printList(head)) + ", node = " + str(a.val))
    Solution().deleteNode(a)
    print("Output: " + str(printList(head)))


main()
