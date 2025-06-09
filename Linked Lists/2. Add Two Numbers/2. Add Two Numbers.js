/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  const dummy = new ListNode();
  let curr = dummy;
  let carry = 0;

  while (l1 || l2) {
    const curr1 = l1 ? l1.val : 0;
    const curr2 = l2 ? l2.val : 0;

    let summ = curr1 + curr2 + carry;
    carry = Math.floor(summ / 10);
    summ %= 10;

    curr.next = new ListNode(summ);
    curr = curr.next;

    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
  }

  if (carry) curr.next = new ListNode(carry);
  return dummy.next;
};

// Time: O(n)
// Space: O(1)
