# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited={0, }

        # def dfs(k):
        #     for room in rooms[k]:
        #         if room not in visited:
        #             visited.add(room)
        #             dfs(room)
        # dfs(0)
        # return len(visited)==len(rooms)
        visited=set()
        que=deque([0])

        while que:
            node = que.popleft()
            visited.add(node)
            for nei in rooms[node]:
                if nei not in visited:
                    que.append(nei)
        # print(visited)
        return len(visited)==len(rooms)