class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = set()
        n = len(rooms)

        q = deque()
        q.append(0)     
        unlocked.add(0)   
        while q:
            r = q.popleft()

            if not rooms[r]:
                continue
            for k in rooms[r]:
                if k in unlocked:
                    continue
                q.append(k)
                unlocked.add(k)

        return len(unlocked) == n