# 2095. Delete the Middle Node of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        cur = head
        if l == 1:
            return None
        for i in range(l // 2 - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head