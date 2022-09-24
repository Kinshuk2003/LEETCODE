class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        sp=['!','@','#','$','%','^','&','*','(',')','-','+']
        u=0
        l=0
        n=0
        s=0
        x=""
        if len(password) >=8:
            for i in password:
                if i.isupper():
                    u +=1
                elif i.islower():
                    l +=1
                elif i.isdigit():
                    n +=1
                elif i in sp:
                    s +=1
                if x == i:
                    return False
                else:
                    x=i
            if u>0 and l>0 and n>0 and s>0:
                return True
        else:
            return False
