class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht= {}
        
        for i in nums:
            if i in ht:
                ht[i] +=1
            else:
                ht[i] =1
        
        for i in ht.keys():
            if ht[i]>1:
                return True
        return False