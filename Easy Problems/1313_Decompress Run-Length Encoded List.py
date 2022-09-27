class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n=len(nums)
        z=(n-2)//2
        res=[]
        for i in range(0,z+1):
            freq=nums[2*i]
            val=nums[2*i+1]
            sums=[val]*freq
            res += sums
        return res
