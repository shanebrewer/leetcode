/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sumListHead = null;
        ListNode sumListIndex = null;
        ListNode nextNode = null;
        int carry = 0;
              
        while(l1 != null || l2 != null) {
            int value1, value2 = 0;
            if(l1 == null) {
                value1 = 0;
                value2 = l2.val;
                l2 = l2.next;
            } else if(l2 == null) {
                value1 = l1.val;
                value2 = 0;
                l1 = l1.next;
            } else {
                value1 = l1.val;
                value2 = l2.val;
                l1 = l1.next;
                l2 = l2.next;
            }
                            
            nextNode = new ListNode((value1 + value2 + carry) % 10);
                
            if (value1 + value2 + carry >= 10)
                    carry = 1;
                else
                    carry = 0;