class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(indices)
        ans=[None]*n
        str=""
        for i in range(n):
            a=indices[i]
            z=s[i:i+1]
            ans[a]=z
        for i in ans:
            str +=i
        return str
