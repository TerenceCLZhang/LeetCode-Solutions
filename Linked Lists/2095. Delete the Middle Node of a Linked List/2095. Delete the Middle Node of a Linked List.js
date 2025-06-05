/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function (head) {
  if (!head || !head.next) return null;

  let slow = head;
  let fast = head.next.next;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  slow.next = slow.next.next;

  return head;
};

// Time: O(n)
// Space: O(1)
