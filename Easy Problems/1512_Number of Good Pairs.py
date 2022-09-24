class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs=0
        c={}
        for i in nums:
            if i in c:
                c[i] +=1
            else:
                c[i]=1
        for i in c:
            val=c[i]
            pairs += ((val*(val-1))//2)
        return pairs
