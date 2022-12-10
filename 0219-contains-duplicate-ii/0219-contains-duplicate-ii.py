class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        newset=set()
        start=0
        end=1
        newset.add(nums[start])
        while(end<n):
            if nums[end] in newset:
                if (end-start) <=k:
                    return True
                else:
                    end +=1
                    start +=1
            else:
                newset.add(nums[end])
                if (end-start)>=k:
                    newset.remove(nums[start])
                    start +=1
                end +=1
        
        return False