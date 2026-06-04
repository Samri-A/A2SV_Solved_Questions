from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visted = set()
        visted.add(0)

        queue = deque([0])

        while queue:

            current = queue.popleft()

            for key in rooms[current]:
                if key not in visted:
                    queue.append(key)
                    visted.add(key)

        return len(visted) == len(rooms)