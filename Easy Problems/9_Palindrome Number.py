class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        p=0
        while n != 0 :
            r= n%10
            n=int(n/10)
            p = p*10 + r
        if p == x :
            return True
        else:
            return False
