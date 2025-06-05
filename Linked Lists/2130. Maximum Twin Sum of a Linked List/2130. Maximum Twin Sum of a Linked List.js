/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function (head) {
  let fast = head.next.next;
  let slow = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  let prev = null;
  slow = slow.next;
  while (slow) {
    const temp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = temp;
  }

  let max_sum = 0;
  let left = head;
  let right = prev;
  while (right) {
    max_sum = Math.max(max_sum, left.val + right.val);
    left = left.next;
    right = right.next;
  }

  return max_sum;
};

// Time: O(n)
// Space: O(1)
