# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            curr = head
            length = 1
            while curr.next:
                curr = curr.next
                length += 1
            return length

        length_a = get_length(headA)
        length_b = get_length(headB)

        while length_a > length_b:
            headA = headA.next
            length_a -= 1

        while length_b > length_a:
            headB = headB.next
            length_b -= 1

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None

# Time: O(n + m)
# Space: O(1)
