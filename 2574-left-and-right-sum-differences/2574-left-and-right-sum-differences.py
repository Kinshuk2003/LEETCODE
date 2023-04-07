class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        leftSum = [0]*length
        rightSum = [0]*length
        answer =[0]*length
        for i in range(0,length-1):
            leftSum[i+1] = leftSum[i]+nums[i]
        
        for i in range(length-1,0,-1):
            rightSum[i-1] = rightSum[i]+nums[i]
            
        for i in range(0,length):
            answer[i] = abs(leftSum[i]-rightSum[i])
        
        return answer
        
            
        