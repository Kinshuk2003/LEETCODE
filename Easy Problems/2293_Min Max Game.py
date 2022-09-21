class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def game(nums: List[int]) -> int:
            n=len(nums)
            if n ==1:
                return nums[0]
            else:
                x=n//2
                newnums=[None]*x
                for i in range(x):
                    if i%2 == 0:
                        newnums[i]=min(nums[2*i],nums[2*i+1])
                    else:
                        newnums[i]=max(nums[2*i],nums[2*i+1])
                return game(newnums)
        return game(nums)
