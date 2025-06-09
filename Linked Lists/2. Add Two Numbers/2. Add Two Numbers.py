# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0

        while l1 or l2:
            curr1 = l1.val if l1 else 0
            curr2 = l2.val if l2 else 0
    
            summ = curr1 + curr2 + carry
            carry = summ // 10
            summ %= 10

            curr.next = ListNode(summ)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next

# Time: O(n)
# Space: O(1)