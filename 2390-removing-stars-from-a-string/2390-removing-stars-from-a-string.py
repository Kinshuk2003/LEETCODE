class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
    
        for i in s:
            
            if i == "*" and stack == []:
                continue
            elif i =="*":
                stack.pop()
            else:
                stack.append(i)
        
        ans = "".join(stack)
        
        return ans
        
        
        
        