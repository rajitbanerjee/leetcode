package mergeSortedLists;

public class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof ListNode) {
            ListNode node = (ListNode) o;
            return node.val == val;
        } else {
            return false;
        }
    }
}