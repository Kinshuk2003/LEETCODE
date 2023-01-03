class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        add=[]
        for i in range(len(strs)):
            x= list(strs[i])
            add.append(x)
        
        for j in range(len(add[0])):
            x=0
            for i in range(len(add)):
                if i ==0:
                    x= ord(add[i][j])
                
                y=ord(add[i][j])
                if y< x:
                    c +=1
                    break
                else:
                    x=y
        
        return c