/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;

        ListNode curr = head;

        // while (curr != null && curr.next != null) {
        //     if (curr.val == curr.next.val) {
        //         curr.next = curr.next.next;
        //     } else {
        //         curr = curr.next;
        //     }
        // }

        while (curr != null) {
            ListNode temp = curr.next;

            while (temp != null && temp.val == curr.val) {
                temp = temp.next;
            }

            curr.next = temp;

            curr = temp;
        }

        return head;
    }
}