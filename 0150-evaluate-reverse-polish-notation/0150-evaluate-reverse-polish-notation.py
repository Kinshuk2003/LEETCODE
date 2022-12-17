class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper=["+","-","*","/"]
        n=len(tokens)
    
        for i in range(n):
            if tokens[i] in oper:
                b=stack.pop()
                a=stack.pop()
                c=0
                if tokens[i]=="+":
                    c=a+b
                elif tokens[i] == "-":
                    c=a-b
                elif tokens[i] =="*":
                    c=a*b
                else:
                    c=int(a/b)
                
                stack.append(c)
                
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]
                
        