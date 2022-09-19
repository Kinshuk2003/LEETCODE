class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[]
        for i in range(len(matrix[0])):
            transpose.append([])
            for j in range(len(matrix)):
                transpose[i].append(matrix[j][i])
                
        return transpose
