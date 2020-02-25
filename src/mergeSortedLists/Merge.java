package mergeSortedLists;

public class Merge {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merged = new ListNode(0);
        merged.next = list1;
        ListNode list3 = merged;

        // merge list 2 into list 1
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                list3 = list1;
                list1 = list1.next;
            } else {
                list3.next = list2;
                list2 = list2.next;
                list3 = list3.next;
                list3.next = list1;
            }
        }

        if (list2 != null) {
            list3.next = list2;
        }

        return merged.next;
    }
}
