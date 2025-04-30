# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp=[]
        heapify(hp)
        for stone in stones:
            heapq.heappush(hp, -stone)
        # hp.reverse()
        # print(hp)
        while len(hp) > 1:
            num1=-hp[0]
            heapq.heappop(hp)
            num2=-hp[0]
            heapq.heappop(hp)

            if num1 != num2:
                heapq.heappush(hp, -(num1 - num2))
        # print(-hp[0])
        if hp:
            return -hp[0]
        return 0
        


