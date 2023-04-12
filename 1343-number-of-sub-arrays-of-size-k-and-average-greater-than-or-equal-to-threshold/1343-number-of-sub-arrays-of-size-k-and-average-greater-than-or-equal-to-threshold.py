class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count =0
        n= len(arr)
        s =0
        for i in range(0,k):
            s += arr[i]
        
        if ((s//k) >= threshold):
            count +=1
        
        for i in range(k,n):
            s -= arr[i-k]
            s += arr[i]
            
            if ((s//k) >= threshold):
                count +=1
                
        
        return count
            
        
        