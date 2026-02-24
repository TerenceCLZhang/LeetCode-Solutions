# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        front = head
        back = prev
        while back:
            if front.val != back.val:
                return False
            front = front.next
            back = back.next

        return True
