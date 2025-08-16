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
var insertGreatestCommonDivisors = function (head) {
  const gcd = (a, b) => {
    while (b) {
      [a, b] = [b, a % b];
    }
    return a;
  };

  curr = head;
  while (curr && curr.next) {
    const gcdVal = gcd(curr.val, curr.next.val);
    curr.next = new ListNode(gcdVal, curr.next);
    curr = curr.next.next;
  }
  return head;
};
