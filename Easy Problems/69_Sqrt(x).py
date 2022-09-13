class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x ==1 or x==2:
            return 1
        low=0
        high=x//2
        mid=(low+high)//2
        while low <= high:
            if mid*mid == x:
                return int(mid)
            elif mid*mid < x:
                low = mid+1
            else:
                high = mid-1
            mid=(low+high)//2
        return int(mid)
