# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getGCD(a, b):
            while b:
                a, b = b, a % b
            return a

        curr = head
        while curr and curr.next:
            gcd = getGCD(curr.val, curr.next.val)
            curr.next = ListNode(gcd, curr.next)
            curr = curr.next.next
        return head

# Time: O(n log m)
# Space: O(1)
# Where m = min(a, b)