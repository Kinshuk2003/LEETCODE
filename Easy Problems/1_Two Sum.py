class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x= []
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if (i !=j and nums[i] + nums[j] == target) :
                    x= []
                    x.append(i)
                    x.append(j)
                    x.sort()
                    return x
