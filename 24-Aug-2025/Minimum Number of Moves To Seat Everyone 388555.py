# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i, j=0, 0
        ans=0
        while i < len(seats) and j < len(students):
            ans+=abs(seats[i]-students[j])
            i+=1
            j+=1
        return ans