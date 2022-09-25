class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        x=0
        for i in range(len(brackets)):
            if income <= brackets[i][0]:
                x=i
                break
        tax=0.0
        c=0
        if income > brackets[0][0]:
            c=brackets[0][0]
            tax += brackets[0][0]*brackets[0][1]/100
            for i in range(1,x+1):
                if income > brackets[i][0]:
                    z=brackets[i][0]-c
                    c =brackets[i][0]
                    tax += z*brackets[i][1]/100
                else:
                    z=income-c
                    tax += z*brackets[i][1]/100
        
        else:
            tax += income*brackets[0][1]/100
        return tax
