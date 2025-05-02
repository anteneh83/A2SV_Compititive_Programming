# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_hp=[]
        for i in range(len(heights)-1):
            diff=heights[i+1] - heights[i]
            if diff > 0:
                heappush(min_hp, diff)

                if len(min_hp) > ladders:
                    bricks -= heappop(min_hp)
                if bricks < 0:
                    return i
        return len(heights) - 1
