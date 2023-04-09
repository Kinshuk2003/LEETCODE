class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i]
        print(prefix)
        if (prefix[n-1]-nums[0]) == 0:
            return 0
        for i in range(1,n):
            if (prefix[i]-nums[i]) == (prefix[n-1]-prefix[i]):
                return i
        else:
            return -1