class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        print(nums)
        for i in range(0,n):
            
            if nums[i] != i:
                return i
        else:
            return n
