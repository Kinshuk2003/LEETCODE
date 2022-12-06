# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        temp=head
        prev=None
        while temp != None:
            if temp.val == val and prev == None:
                temp=temp.next
                head=temp
                prev=None
            elif temp.val == val:
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        
        return head