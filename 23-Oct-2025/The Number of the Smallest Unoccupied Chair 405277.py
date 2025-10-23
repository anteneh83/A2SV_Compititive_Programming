# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        order = sorted(range(len(times)), key=lambda x: times[x][0])
        # print(order)
        emptySeat, takenSeat = list(range(len(times))), []

        for i in order:
            ar, lv = times[i]

            while takenSeat and takenSeat[0][0] <= ar:
                heappush(emptySeat, heappop(takenSeat)[1])

            seat = heappop(emptySeat)

            if i == targetFriend: return seat

            heappush(takenSeat, (lv, seat))