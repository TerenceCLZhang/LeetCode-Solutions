/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    if (left == right) return head

    const dummy = new ListNode(0, head)
    let left_prev = dummy

    for (let i = 0; i < left - 1; i++) left_prev = left_prev.next

    let prev = null
    let curr = left_prev.next
    for (let i = 0; i < right - left + 1; i++) {
        const temp = curr.next
        curr.next = prev
        prev = curr;
        curr = temp;
    }

    left_prev.next.next = curr
    left_prev.next = prev

    return dummy.next
};

// Time: O(n)
// Space: O(1)