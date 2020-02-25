package mergeSortedLists;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MergeTest {
    @Test
    void testMerge() {
        ListNode list1 = new ListNode(1);
        ListNode a2 = new ListNode(2);
        ListNode a3 = new ListNode(4);
        list1.next = a2;
        a2.next = a3;

        ListNode list2 = new ListNode(1);
        ListNode b2 = new ListNode(3);
        ListNode b3 = new ListNode(4);
        list2.next = b2;
        b2.next = b3;

        ListNode expected = new ListNode(1);
        ListNode m2 = new ListNode(1);
        ListNode m3 = new ListNode(2);
        ListNode m4 = new ListNode(3);
        ListNode m5 = new ListNode(4);
        ListNode m6 = new ListNode(4);
        expected.next = m2;
        m2.next = m3;
        m3.next = m4;
        m4.next = m5;
        m5.next = m6;

        Merge m = new Merge();
        ListNode mergeOutput = m.mergeTwoLists(list1, list2);
        while (mergeOutput != null) {
            assertEquals(expected, mergeOutput);
            mergeOutput = mergeOutput.next;
            expected = expected.next;
        }
    }
}