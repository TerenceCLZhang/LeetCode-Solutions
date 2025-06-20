/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  if (!head) return head;

  const oldToNew = new Map();

  let curr = head;
  while (curr) {
    oldToNew.set(curr, new Node(curr.val, null, null));
    curr = curr.next;
  }

  curr = head;
  while (curr) {
    const copy = oldToNew.get(curr);
    copy.next = oldToNew.get(curr.next) || null;
    copy.random = oldToNew.get(curr.random) || null;
    curr = curr.next;
  }

  return oldToNew.get(head);
};

// Time: O(n)
// Space: O(n)
