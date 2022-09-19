class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=len(nums)
        runningsum = []
        for i in range(1,x+1):
            runningsum.append(sum(nums[:i]))
        return runningsum
