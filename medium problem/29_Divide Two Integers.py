class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isminus=((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0))
        dividend =abs(dividend)
        divisor=abs(divisor)
        quo=0
        q,temp=1,divisor
        while(dividend >= divisor):
            if (dividend >= temp):
                quo +=q
                dividend -=temp
                temp <<=1
                q <<=1
            else:
                temp >>=1
                q >>=1
        if isminus :
            quo = -quo
        return min(max(-2147483648,quo),2147483647)
