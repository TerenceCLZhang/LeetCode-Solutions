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
var getDecimalValue = function (head) {
  let decimal = 0;
  let curr = head;
  while (curr) {
    decimal = (decimal << 1) + curr.val;
    curr = curr.next;
  }
  return decimal;
};

// Time: O(n)
// Space: O(1)
