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

  public ListNode insertGreatestCommonDivisors(ListNode head) {
    ListNode curr = head;
    while (curr != null && curr.next != null) {
      int gcdVal = gcd(curr.val, curr.next.val);
      ListNode temp = curr.next;
      curr.next = new ListNode(gcdVal, curr.next);
      curr.next.next = temp;
      curr = curr.next.next;
    }
    return head;
  }

  private int gcd(int a, int b) {
    while (b > 0) {
      int temp = a;
      a = b;
      b = temp % b;
    }
    return a;
  }
}
