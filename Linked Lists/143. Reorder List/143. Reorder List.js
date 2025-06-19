/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  let fast = head,
    slow = head;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  let prev = null;
  let curr = slow;
  while (curr) {
    const temp = curr.next;
    curr.next = prev;
    prev = curr;
    curr = temp;
  }

  let left = head;
  let right = prev;
  while (right.next) {
    const temp1 = left.next;
    const temp2 = right.next;

    left.next = right;
    right.next = temp1;

    left = temp1;
    right = temp2;
  }
};

// Time: O(n)
// Space: O(1)
