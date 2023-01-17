class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        elesum=0
        digsum=0
        
        for e in nums:
            elesum +=e
            
            while e:
                digsum += (e%10)
                e= e//10
            
        return abs(elesum-digsum)