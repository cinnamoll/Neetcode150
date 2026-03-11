# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        rmv = head
        count = 0
        while count < n:
            curr = curr.next
            count+=1

        if not curr:
            return head.next

        while curr.next:
            curr = curr.next
            rmv = rmv.next
        rmv.next = rmv.next.next
        return head
        