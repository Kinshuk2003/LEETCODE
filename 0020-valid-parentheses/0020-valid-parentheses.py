class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = ['(','{','[']
        close_braces = [ ')','}',']' ]
        stack = []
        for i in s:
            if i in open_braces:
                stack.append(i)
            elif i in close_braces:
                x = close_braces.index(i)
                n=len(stack)
                if (n>0) and (open_braces[x] == stack[n-1]):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False 
        