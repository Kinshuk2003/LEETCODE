class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n=len(students)
        ans =0
        for i in range(0,n):
            ans +=  abs(seats[i]-students[i])
        return ans
