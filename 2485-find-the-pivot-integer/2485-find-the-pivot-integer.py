class Solution:
    def pivotInteger(self, n: int) -> int:
        
        if n==1:
            return 1
        prefix=[1]*n
        
        for i in range(2,n+1):
            prefix[i-1] = prefix[i-2]+ i
        
        pivot=-1
        for i in range(n):
            if prefix[i] == (prefix[n-1]-prefix[i-1]):
                pivot = i+1
        
        return pivot
            
            
        