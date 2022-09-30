class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        z=sum(arr)
        n=len(arr)
        c=3
        while (c<= n):
            for i in range(0,n+1-c):
                x=[arr[i] for i in range(i,i+c)]
                z +=sum(x)
            c +=2
        return z
