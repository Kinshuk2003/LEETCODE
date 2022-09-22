class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la=lb=0
        a, b = headA,headB
        
        while(headA):
            la +=1
            headA = headA.next
        
        while(headB):
            lb +=1
            headB = headB.next
        
        if(la > lb):
            diff=la-lb
            while(diff):
                a = a.next
                diff -=1
        elif(lb > la):
            diff=lb-la
            while(diff):
                b = b.next
                diff -=1
        
        while(a and b):
            if(a == b): return a
            a = a.next
            b = b.next
        return None 
