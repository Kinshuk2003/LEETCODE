class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[]
        arr.append(first)
        n=len(encoded)
        for i in range(0,n):
            z=encoded[i]^arr[i]
            arr.append(z)
        return arr
