# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        print(bisect.bisect_left(heaters, 1))
        def get_max(house):
            pos = bisect.bisect_left(heaters, house)
            left_rad = float('inf') if pos == 0 else house - heaters[pos-1]
            right_rad = float('inf') if pos == len(heaters) else heaters[pos] - house

            return min(left_rad, right_rad)

        ans = 0
        for house in houses:
            ans = max(ans, get_max(house))
        return ans

            