class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val=0
        for i in digits:
            val = val*10 +i
        val=val+1
        temp = [int(i) for i in str(val)]
        return temp
