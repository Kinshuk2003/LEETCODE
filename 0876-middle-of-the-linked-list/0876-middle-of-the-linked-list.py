# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first=head
        count=0
        while first:
            count +=1
            first=first.next

        if count%2==0:
            count=(count/2)
        else:
            count=(count//2)
        
        while(count>0):
            head=head.next
            count -=1
        
        return head
        