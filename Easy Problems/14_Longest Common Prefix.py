class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        low=0
        high=len(min(strs,key=len))
        while low <= high:
            mid = (low+high)//2
            for s in strs[1:]:
                if strs[0][0:mid] != s[0:mid]:
                    high= mid-1
                    break
            else:
                low=mid+1
                print(low,high)
                print(strs[0][0:low-1])
            
        if low > 0:
            return strs[0][0:low-1]
        else:
            return ""
