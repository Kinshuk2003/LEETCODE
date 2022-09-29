class Solution:
    def greatestLetter(self, s: str) -> str:
        greater=[]
        match=[]
        for i in s:
            if i in match:
                continue
            elif i.swapcase() in match:
                if i.isupper():
                    greater.append(i)
                else:
                    greater.append(i.upper())
            else:
                match.append(i)
        s=""
        if len(greater) > 1:
            s= max(greater)
            return s
        elif len(greater) ==1:
            s=greater[0]
            return s
        else:
            return s
