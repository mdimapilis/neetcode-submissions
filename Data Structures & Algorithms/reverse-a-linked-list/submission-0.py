# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        temp = None
        while curr is not None:
            #temp saved as next node
            temp = curr.next
            #curr.next flips direction
            curr.next = prev
            #moving prev to curr node
            prev = curr
            #moving curr forward
            curr = temp
        return prev

        