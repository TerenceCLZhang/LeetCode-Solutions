# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev, slow = slow, temp
        
        # Check compare first and second halves
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l, r = l.next, r.next
        
        return True

# Time: O(n)
# Space: O(1)