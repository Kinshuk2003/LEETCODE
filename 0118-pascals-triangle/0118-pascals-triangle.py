class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result= [[1]]
        
        for i in range(1,numRows):
            ans=[1]
            if len(result[i-1]) < 2:
                ans.append(1)
            else:
                for j in range(1,len(result[i-1])):
                    ans.append(result[i-1][j-1]+result[i-1][j])
                ans.append(1)
            
            result.append(ans)
        
        return result
        